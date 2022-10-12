################################################################################### USED LIBRARIES ################################################################################################
import pandas as pd
import numpy as np
import pickle
from math import isnan
from datetime import datetime, timedelta
import re
################################################################################### HELPER FUNCTIONS ##############################################################################################
def to_snake(text):
    '''
    Converts given text to snake_case.

    Parameters
    ----------
    text : text to be converted

    Returns
    -------
    text : new text in snake_case
    '''
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text

def add_period_to_col(df, col, period):
    '''
    Extracts selected period from datetime and creates a new period column(s).

    Parameters
    ----------
    df : dataframe on which the function will be applied
    col : column new name
    period : period to be extracted

    Returns
    -------
    df : dataframe with new period column(s)
    '''
    if period == 'day':
        df[col] = df.apply(lambda x: x['date'].day if isnan(x[col]) else x[col],axis=1)
    elif period == 'week':
        df[col] = df.apply(lambda x: x['date'].week if isnan(x[col]) else x[col],axis=1)
    elif period == 'month':
        df[col] = df.apply(lambda x: x['date'].month if isnan(x[col]) else x[col],axis=1)
    elif period == 'year':
        df[col] = df.apply(lambda x: x['date'].year if isnan(x[col]) else x[col],axis=1)
    else:
        raise ValueError('Please select period: day, week, month or year')
    return df


def to_int_64(df,change_types_list):
    '''
    Changes data type to int64.

    Parameters
    ----------
    df : dataframe on which the function will be applied
    change_types_list : list of columns on which the function will be applied

    Returns
    -------
    df : dataframe with new column types
    '''
    for i in change_types_list:
        df[f'{i}'] = df[f'{i}'].astype('int64')
    return df


def nature_encode(df, col, div_period):
    '''
    Applies a Nature Cyclical Transformation, where each period
    is a combination of sin and cos.

    Parameters
    ----------
    df : dataframe on which the function will be applied
    col : period column on which the function will be applied
    div_period : amount of periods until the cycle restarts (e.g. month=12, week=7, etc)

    Returns
    -------
    None
    '''
    df[col + '_sin'] = np.sin(2 * np.pi * df[col]/div_period)
    df[col + '_cos'] = np.cos(2 * np.pi * df[col]/div_period)
    return None

################################################################################### ROSSMANN CLASS ###############################################################################################
class Rossmann(object):
        def __init__(self):
                self.home_path=''
                self.competition_distance_scaler   = pickle.load(open(self.home_path + 'parameters/competition_distance_scaler.pkl', 'rb')) # Loading transformed competition_distance
                self.competition_time_month_scaler = pickle.load(open(self.home_path + 'parameters/competition_time_month_scaler.pkl', 'rb')) # Loading transformed competition_time_month
                self.promo_time_week_scaler        = pickle.load(open(self.home_path + 'parameters/promo_time_week_scaler.pkl', 'rb')) # Loading transformed promo_time_week
                self.year_scaler                   = pickle.load(open(self.home_path + 'parameters/year_scaler.pkl', 'rb')) # Loading transformed year
                self.store_type_scaler             = pickle.load(open(self.home_path + 'parameters/store_type_scaler.pkl', 'rb')) # Loading transformed store_type

        def data_cleaning(self, df1):
                # Applying to_snake function
                cols = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday', 'StoreType',  'Assortment',
                        'CompetitionDistance','CompetitionOpenSinceMonth','CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'PromoInterval']
                snake = lambda x: to_snake(x)
                new_cols = list(map(snake, cols))

                # Renaming
                df1.columns = new_cols

                # Changing data types
                df1['date'] = pd.to_datetime(df1['date'])

                # Dealing with competition_distance
                max_comp = 3*df1['competition_distance'].max()
                df1['competition_distance'] = df1['competition_distance'].apply(lambda x: max_comp if isnan(x) else x)

                # Applying add_period_to_col function
                df1 = add_period_to_col(df1, 'competition_open_since_month', 'month')
                df1 = add_period_to_col(df1, 'competition_open_since_year', 'year')
                df1 = add_period_to_col(df1, 'promo2_since_week', 'week')
                df1 = add_period_to_col(df1, 'promo2_since_year', 'year')

                # Dealing with months
                month_map = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
                df1['promo_interval'].fillna(0, inplace=True)
                df1['month_map'] = df1['date'].dt.month.map(month_map)
                df1['is_promo'] = df1[['promo_interval', 'month_map']].apply(lambda x: 0 if x['promo_interval'] == 0 else 1 if x['month_map'] in x['promo_interval'].split( ',' ) else 0, axis=1)

                # Converting to int64
                df1 = to_int_64(df1, ['competition_open_since_month', 'competition_open_since_year','promo2_since_week', 'promo2_since_year'])

                # Returns the cleaned data
                return df1

        def feature_engineering(self, df2):
                # Dealing with dates
                df2['day'] = df2['date'].dt.day
                df2['week_of_year'] = df2['date'].dt.isocalendar().week.astype('int64')
                df2['year_week'] = df2['date'].dt.strftime('%Y-%W')
                df2['month'] = df2['date'].dt.month
                df2['year'] = df2['date'].dt.year

                # Dealing with competition_since
                df2['competition_since'] = df2.apply(lambda x: datetime(year=x['competition_open_since_year'],month=x['competition_open_since_month'],day=1), axis=1)
                df2['competition_time_month'] = ((df2['date'] - df2['competition_since'])/30).apply(lambda x: x.days).astype(int)

                # Dealing with promo_since
                df2['promo_since'] = df2['promo2_since_year'].astype(str) +'-' +df2['promo2_since_week'].astype(str)
                df2['promo_since'] = df2['promo_since'].apply(lambda x: datetime.strptime(x + '-1', '%Y-%W-%w') - timedelta(days=7))
                df2['promo_time_week'] = ((df2['date'] - df2['promo_since'])/7).apply(lambda x: x.days).astype(int)

                # Dealing with assortment
                df2['assortment'] = df2['assortment'].apply(lambda x: 'basic' if x=='a' else 'extra' if x=='b' else 'extended')
                # Dealing with state_holiday
                df2['state_holiday'] = df2['state_holiday'].apply(lambda x: 'public_holiday' if x=='a' else 'easter_holiday' if x=='b' else 'christmas' if x=='c' else 'regular_day')

                # Converting to int64 again
                df2 = to_int_64(df2, ['competition_open_since_month', 'competition_open_since_year','promo2_since_week', 'promo2_since_year'])

                # Filtering rows
                df2 = df2[df2['open']!=0]

                # Filtering cols
                cols_drop = ['open', 'promo_interval', 'month_map']
                df2 = df2.drop(cols_drop, axis=1)

                # Returns the transformed data
                return df2

        def data_preparation(self, df5):
                # Getting the transformed competition_distance, competition_time_month, promo_time_week, year
                df5['competition_distance'] = self.competition_distance_scaler.transform(df5[['competition_distance']].values)
                df5['competition_time_month'] = self.competition_time_month_scaler.transform(df5[['competition_time_month']].values)
                df5['promo_time_week'] = self.promo_time_week_scaler.transform(df5[['promo_time_week']].values)
                df5['year'] = self.year_scaler.transform(df5[['year']].values)

                # One Hot Encoding (state_holiday)
                df5 = pd.get_dummies(df5, prefix=['state_holiday'], columns=['state_holiday'])

                # Label Encoding (store_type)
                df5['store_type'] = self.store_type_scaler.transform(df5['store_type'])

                # Ordinal Encoding (assortment)
                assortment_dict = {'basic': 1, 'extra': 2, 'extended': 3}
                df5['assortment'] = df5['assortment'].map(assortment_dict)

                # Response variable transformation
                # df5['sales'] = np.log1p(df5['sales'])

                # Applying nature_encode function
                nature_encode(df5, 'day_of_week', 7)
                nature_encode(df5, 'month', 12)
                nature_encode(df5, 'day', 30)
                nature_encode(df5, 'week_of_year', 52)

                # Cols selected to train the ML model
                cols_selected = ['store','promo','store_type','assortment','competition_distance','competition_open_since_month','competition_open_since_year',
                                 'promo2','promo2_since_week','promo2_since_year','competition_time_month','promo_time_week','day_of_week_sin','day_of_week_cos',
                                 'month_sin','month_cos','day_sin','day_cos','week_of_year_sin','week_of_year_cos']

                # Returns the transformed data with selected cols
                return df5[cols_selected]

        def get_prediction(self, model, original_data, test_data):
            # Prediction
            pred = model.predict(test_data)
            original_data['prediction'] = np.expm1(pred)

            # Convert to json
            return original_data.to_json(orient='records', date_format='iso')
