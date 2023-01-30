<h1 align="center"> Creating a Bot that Predicts Rossmann Future Sales</h1>

<p align="center">A Regression Project</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/195202224-01bfd468-9f1c-4e83-af60-b101312a98e3.svg" alt="drawing" width="700"/>
</p>

*Obs: The business problem is fictitious, although both company and data are real.*

*The in-depth Python code explanation is available in [this](https://github.com/brunodifranco/project-rossmann-sales/blob/main/rossmann.ipynb) Jupyter Notebook.*

# 1. **Rossmann and Business Problem**
<p align="justify"> Rossmann is one of the largest drug store chains in Europe, with operations in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain. Their sales can be influenced by promotions, competition, school and state holidays, seasonality, locality, etc.</p>

This **Data Science** project is focused on solving one problem: 

- ### **Rossmann CEO is requiring a sales prediction of the next six weeks for each store, in order to determine the best resource allocation for each store renovation.**

# 2. **Data Overview**
The data was collected from [Kaggle](https://www.kaggle.com/). This [dataset](https://www.kaggle.com/competitions/rossmann-store-sales/data) contains historical sales data for 1,115 Rossmann stores. The initial features descriptions are available below:

| Feature | Definition |
|---|---|
| Id | an Id that represents a (Store, Date) duple within the dataset.|
| Store | a unique Id for each store.|
| Sales | the turnover for any given day.|
| DayOfWeek | day of week on which the sale was made (e.g. DayOfWeek=1 -> monday, DayOfWeek=2 -> tuesday, etc).|
| Date | date on which the sale was made.|
| Customers | the number of customers on a given day.|
| Open | an indicator for whether the store was open: 0 = closed, 1 = open.|
| StateHoliday | indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None.|
| SchoolHoliday  | indicates if the (Store, Date) was affected by the closure of public schools.|
| StoreType  | differentiates between 4 different store models: a, b, c, d.|
| Assortment | describes an assortment level: a = basic, b = extra, c = extended.|
| CompetitionDistance | distance in meters to the nearest competitor store.|
| CompetitionOpenSince(Month/Year)| gives the approximate year and month of the time the nearest competitor was opened.|
| Promo | indicates whether a store is running a promo on that day.|
| Promo2 | Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating.|
| Promo2Since(Year/Week)| describes the year and calendar week when the store started participating in Promo2.|
| PromoInterval | describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store.|

# 3. **Assumptions**
- Customers column was dropped, because for now there's no information about the amount of customers six weeks into the future. 
- The NaN's in CompetitionDistance were replaced by 3 times the maximum CompetitionDistance in the dataset, because the observations with NaN's are likely stores that are too far, which means there's no competition.
- Some new features were created in order to best describe the problem: 

| New Feature | Definition |
|---|---|
| day/week_of_year/year_week/month/year | day/week_of_year/year_week/month/year extracted from 'date' column.|
| day/day_of_week/week_of_year/month(sin/cos) | sin/cos component of each period, to capture their cyclical behavior.|
| competition_time_month| amount of months from competition start.|
| promo_time_week | time in weeks from when the promotion was active.|
| state_holiday(christmas/easter_holiday/public_holiday/regular_day)| indicates wheter the sale was made in christmas, easter, public holiday or regular day.|

# 4. **Solution Plan**
## 4.1. How was the problem solved?

<p align="justify"> To predict sales values for each store (six weeks in advance) a Machine Learning model was applied. To achieve that, the following steps were performed: </p>

- <b> Understanding the Business Problem </b> : Understanding the reasons why Rossmann's CEO was requiring that task, and plan the solution. 

- <b> Collecting Data </b>: Collecting Rossmann store and sales data from Kaggle.

- <b> Data Cleaning </b>: Renaming columns, changing data types and filling NaN's. 

- <b> Feature Engineering </b>: Creating new features from the original ones, so that those could be used in the ML model. 

- <p align="justify"> <b> Exploratory Data Analysis (EDA) </b>: Exploring the data in order to obtain business experience, look for useful business insights and find important features for the ML model. The top business insights found are available in <a href="https://github.com/brunodifranco/project-rossmann-sales#5-top-business-insights"> Section 5 </a>. </p>

- <b> Data Preparation </b>: Applying <a href="https://www.atoti.io/articles/when-to-perform-a-feature-scaling/">Normalization and Rescaling Techniques</a> in the data, as well as <a href="https://www.geeksforgeeks.org/feature-encoding-techniques-machine-learning/">Enconding Methods</a> and Response Variable Transformation.

- <b> Feature Selection </b>: Selecting the best features to use in the ML model by applying the <a href="https://www.section.io/engineering-education/getting-started-with-boruta-algorithm/">Boruta Algorithm</a>. 

- <p align="justify"> <b> Machine Learning Modeling </b>: Training Regression Algorithms with time series cross-validation. The best model was selected to be improved via Hyperparameter Tuning. More information in <a href="https://github.com/brunodifranco/project-rossmann-sales#6-machine-learning-models">Section 6 </a>. </p>

- <b> Model Evaluation </b>: Evaluating the model using four metrics: MAE, MAPE, RMSE and R<sup>2</sup>. 

- <b> Financial Results </b>: Translating the ML model's statistical performance to financial and business performance.

- <p align="justify"> <b> Model Deployment (Telegram Bot) </b>: Implementation of a Telegram Bot that will give you the prediction of any given available store number. This is the project's <b>Data Science Product</b>, and it can be accessed from anywhere. More information in <a href="https://github.com/brunodifranco/project-rossmann-sales#7-model-deployment"> Section 7 </a>. </p>
  
## 4.2. Tools and techniques used:
- [Python 3.9.12](https://www.python.org/downloads/release/python-3912/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) and [Sklearn](https://scikit-learn.org/stable/).
- [Jupyter Notebook](https://jupyter.org/) and [VSCode](https://code.visualstudio.com/).
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) and [Python API's](https://realpython.com/api-integration-in-python/).  
- [Render Cloud](https://render.com/) and [Telegram Bot](https://core.telegram.org/bots/api).
- [Git](https://git-scm.com/) and [Github](https://github.com/).
- [Exploratory Data Analysis (EDA)](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15). 
- [Techniques for Feature Selection](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/).
- [Regression Algorithms (Linear and Lasso Regression; Random Forest, XGBoost and LGBM Regressors)](https://towardsdatascience.com/7-of-the-most-commonly-used-regression-algorithms-and-how-to-choose-the-right-one-fc3c8890f9e3).
- [Cross-Validation Methods](https://medium.com/@soumyachess1496/cross-validation-in-time-series-566ae4981ce4), [Hyperparameter Optimization](https://towardsdatascience.com/7-hyperparameter-optimization-techniques-every-data-scientist-should-know-12cdebe713da) and [Algorithms Performance Metrics (RMSE, MAE, MAPE, R2)](https://machinelearningmastery.com/regression-metrics-for-machine-learning/#:~:text=There%20are%20three%20error%20metrics,Mean%20Absolute%20Error%20(MAE)).

# 5. **Top Business Insights**

 - ### 1st - Stores with basic assortment level are the ones that sell more.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964237-f82c668c-3ea3-4373-b562-d18ab0a1f6f4.png" alt="drawing" width="800"/>
</p>

--- 
- ### 2nd - Stores with higher number of close competitors sell more.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964211-f1215de3-795c-4c2b-9d73-071b50a3cd96.png" alt="drawing" width="850"/>
</p>

---
- ### 3rd - Easter Holiday has the highest average sales, in comparison to other periods.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964219-b73605bc-87f0-4b0e-9cf9-8026d32d49d5.png" alt="drawing" width="850"/>
</p>

---
- ### 4th - Stores sell less during the second semester of each year.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964226-54bbb2b2-424e-4128-b958-b82ded2581d5.png" alt="drawing" width="850"/>
</p>

---
- ### 5th - Stores Sell more after the 10th day of each month.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964232-b28632ac-2e6d-4e5b-a302-1c5f2c533d3d.png" alt="drawing" width="850"/>
</p>

# 6. **Machine Learning Models**

<p align="justify"> This was the most fundamental part of this project, since it's in ML modeling where the sales predictions for each store can be made. Six models were trained using time series cross-validation: </p>

- Average Model (used as a baseline model)
- Linear Regression
- Lasso Regression (Regularized Linear Regression)
- Random Forest Regressor
- XGBoost Regressor
- Light GBM Regressor

The initial performance for all six algorithms are displayed below (sorted by RMSE):

<div align="center">

| **Model Name** | **MAE** | **MAPE** | **RMSE** | **R<sup>2</sup>** |
|:---:|:---:|:---:|:---:|:---:|
| LGBM Regressor | 833.23 +/- 121.0 | 0.1178 +/- 0.0093 | 1197.68 +/- 176.39 | 0.8467 +/- 0.0237 |
| Random Forest Regressor | 838.84 +/- 219.91 | 0.1162 +/- 0.0233 | 1257.62 +/- 321.14 | 0.8409 +/- 0.0527 |
| XGBoost Regressor | 900.29 +/- 152.53 | 0.1273 +/- 0.0155 | 1293.45 +/- 214.31 | 0.8322 +/- 0.0334 |
| Average Model (Baseline) | 1354.8 | 0.2064 | 1835.14 | 0.6366 |
| Linear Regression | 2081.72 +/- 295.57 | 0.3026 +/- 0.0166 | 2953.15 +/- 468.22 | 0.1353 +/- 0.0721 |
| Lasso Regression | 2116.42 +/- 341.46 | 0.292 +/- 0.0118 | 3058.12 +/- 504.18 | 0.0742 +/- 0.0834 |

</div>

<p align="justify"> Both Linear Regression and Lasso Regression have worst performances in comparison to the simple Average Model. This shows a nonlinear behavior in our dataset, hence the use of more complex models, such as Random Forest, XGBoost and Light GBM. </p>

<p align="justify"> <b> The LGBM model was chosen for Hyperparameter Tuning, since it has the lowest RMSE. Even if we look into other metrics, such as MAPE (on which Random Forest has the best performance), LGBM would still be better to use, because it's much faster to train and tune </b>. </p>

After tuning LGBM's hyperparameters using <a href="https://towardsdatascience.com/hyper-parameter-tuning-in-python-1923797f124f">Random Search</a> the model performance has improved: 

<div align="center">
	
| **Model Name** | **MAE** | **MAPE** | **RMSE** | **R<sup>2</sup>** |
|:---:|:---:|:---:|:---:|:---:|
| LGBM Regressor | 617.54000 | 0.08940 | 921.52000 | 0.90840 |
	
</div>

## <i>Metrics Definition and Interpretation</i>

<div align="center">

| **_Metric_** | **_Definition_** |
|:---:|:---:|
| _MAE_ | _Mean Absolute Error_ |
| _MAPE_ | _Mean Absolute Percentage Error_ |
| _RMSE_ | _Root Mean Squared Error_ |
| _R<sup>2</sup>_ | _Coefficient of Determination_ |

</div>

<p align="justify"> <i> R<sup>2</sup> basically show how well the sales are being predicted by the model, and alongside RMSE isn't the best metric to translate into financial performance, despite being key to check statistical performance. 

Both MAE and MAPE are really useful in explaining the model's business performance. MAE shows how much the model prediction is wrong on average, while MAPE shows how much the model prediction is wrong on average percentage-wise. </i> </p>

## 6.1. Brief Financial Results:

<p align="justify"> Below there are displayed two tables with brief financial results given by the LGBM model, as the complete financial results will be explained in the next <a href="https://github.com/brunodifranco/project-rossmann-sales#7-model-deployment"> section </a>. </p>

<p align="justify"> A couple interesting metrics to evaluate the financial performance of this solution (<b>LGBM Model</b>) is the MAE and MAPE. Below there's a table with a few stores metrics: </p>
<div align="center">

| **Store** | **Predictions (€)** | **Worst Scenario (€)** | **Best Scenario (€)** | **MAE (€)** | **MAPE** |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 161,274.69 | 160,988.99 | 161,560.39 | 285.69937 | 0.06472 |
| 2 | 175,549.76 | 175,192.06 | 175,907.47 | 357.70668 | 0.07338 |
| 3 | 259,576.04 | 259,077.04 | 260,075.03 | 498.99756 | 0.07215 |
| ... | ... | ... | ... | ... | ... |
| 1113 | 238,353.17 | 237,841.04 | 238,865.30 | 512.12600 | 0.07852 |
| 1114 | 769,997.75 | 767,598.11 | 772,397.39 | 2399.63754 | 0.10164 |
| 1115 | 254,766.52 | 254,227.68 | 255,305.36 | 538.83848 | 0.07576 |
</div>

<p align="justify"> According to this model, the sales sum for all stores over the next six weeks is: </p>

<div align="center">

| **Scenario (€)** | **Total Sales of the Next 6 Weeks (€)** |
|:---:|:---:|
| Prediction  | 283,786,860.62 |
| Worst Scenario | 283,094,186.26 |
| Best Scenario | 284,479,534.97 |

</div>

# 7. **Model Deployment**

<p align="justify">  As previously mentioned, the complete financial results can be consulted by using the Telegram Bot. The idea behind this is to facilitate the access of any store sales prediction, as those can be checked from anywhere and from any electronic device, as long as internet connection is available.  
The bot will return you a sales prediction over the next six weeks for any available store, <b> all you have to do is send him the store number in this format "/store_number" (e.g. /12, /23, /41, etc) </b>. If a store number if non existent the message "Store not available" will be returned, and if you provide a text that isn't a number the bot will ask you to enter a valid store id. 

 <div align="center">

|         **Click below to chat with the Rossmann Bot**        |
|:------------------------:|
|        [![image](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/rossmann_project_api_bot)
</div>

<i> Because the deployment was made in a free cloud (Render) it could take a few minutes for the bot to respond, <b> in the first request. </b> In the following requests it should respond instantly. </i>

</p>

# 8. **Conclusion**
In this project the main objective was accomplished:

 <p align="justify"> <b> A model that can provide good sales predictions for each store over the next six weeks was successfully trained and deployed in a Telegram Bot, which fulfilled CEO' s requirement, for now it's possible to determine the best resource allocation for each store renovation. </b> In addition to that, five interesting and useful insights were found through Exploratory Data Analysis (EDA), so that those can be properly used by Rossmann CEO. </p>
 
# 9. **Next Steps**
<p align="justify"> Further on, this solution could be improved by a few strategies:

 - Using <a href="https://towardsdatascience.com/an-introduction-to-time-series-analysis-with-arima-a8b9c9a961fb">ARIMA</a> to predict the amount of customers over the next six weeks, so that the customers column could be added to the final model. </p>
 
 - Tune even more the regression algorithm, by applying a <a href="https://machinelearningmastery.com/what-is-bayesian-optimization/">Bayesian Optimization</a> for instance. 
  
 - Try other regression algorithms to predict the sales for each store.
 
 - Use different models for the stores on which it's more difficult (higher MAE and MAPE) to predict the sales.

# Contact

- brunodifranco99@gmail.com
- [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/BrunoDiFrancoAlbuquerque/)
