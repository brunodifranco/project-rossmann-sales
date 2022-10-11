<h1 align="center">nome do projeto</h1>

<p align="center">Data Science Full Project</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191957066-c9699023-eb0e-4e20-9508-869ee8038ecf.jpg" alt="drawing" width="750"/>
</p>

# 1. **Rossmann and Business Problem**
<p align="justify"> Rossmann is one of the largest drug store chains in Europe, with operations in Germany, Poland, Hungary, Czech Republic, Turkey, Albania, Kosovo and Spain. Their sales can be influenced by promotions, competition, school and state holidays, seasonality, locality, etc.</p>

*Obs: The business problem is fictitious, although both company and data are real.*

This **Data Science** project is focused on solving one problem: 

- ### **Rossmann CEO is requiring a sales prediction of the next six weeks for each store, in order to determine the best resources allocation for each store renovation.**

*The in-depth Python code explanation is available in [this](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/jupyter-house-rocket.ipynb) Jupyter Notebook.*

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

- Understanding the Business Problem
- Collecting Data
- Data Cleaning
- Feature Engineering 
- Exploratory Data Analysis (EDA)
- Data Preparation
- Machine Learning Modeling
- Model Evaluation
- Financial Results
- Model Deployment (Telegram Bot)

 [![image](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/rossmann_project_api_bot)
  
## 4.2. Tools and techniques used:
- [Python 3.9.12](https://www.python.org/downloads/release/python-3912/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Plotly](https://plotly.com/python/) and [Geopandas](https://geopandas.org/en/stable/).
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
  <img src="https://user-images.githubusercontent.com/66283452/194964237-f82c668c-3ea3-4373-b562-d18ab0a1f6f4.png" alt="drawing" width="750"/>
</p>

--- 
- ### 2nd - Stores with higher number of close competitors sell more.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964211-f1215de3-795c-4c2b-9d73-071b50a3cd96.png" alt="drawing" width="750"/>
</p>

---
- ### 3rd - Easter Holiday has the highest average sales, in comparison to other periods.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964219-b73605bc-87f0-4b0e-9cf9-8026d32d49d5.png" alt="drawing" width="750"/>
</p>

---
- ### 4th - Stores sell less during the second semester of each year.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964226-54bbb2b2-424e-4128-b958-b82ded2581d5.png" alt="drawing" width="750"/>
</p>

---
- ### 5th - Stores Sell more after the 10th day of each month.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/194964232-b28632ac-2e6d-4e5b-a302-1c5f2c533d3d.png" alt="drawing" width="750"/>
</p>

# 6. **Machine Learning Models**






# 7. **Model Deployment and Financial Results**

<p align="justify"> Three interesting metrics to evaluate the financial performance for this solution is the profit mean and median (grouped by ad_season, zipcode and ad_season with zipcode), as well as the total profit. This in-depth information can be found in <a href="https://github.com/brunodifranco/project-house-rocket-insights/tree/main/financial-results">here</a>. As for the profit for each property it can be checked in the <a href="https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/">House Rocket Cloud App</a>, where filters can also be applied for better visualization. </p>

<p align="justify"> <b> If this feasible solution strategy used in this project were applied by House Rocket the total obtained profit would be US$ 473,094,328.48, with an average profit of US$ 45,337.26 per property. The main profit metrics are displayed below: </b></p>

<div align="center">
 
| **Metric** | **US$** |
|---|---|
| Total Profit | 473,094,328.48 |
| Profit Mean | 45,337.26 |
| Profit Median | 39,995.00 |
| Min Profit | 8,217.50 |
| Max Profit | 350,036.80 | 

</div>

# 8. **Conclusion**
In this project the two main objectives were accomplished:

 - A feasible solution was found for both business problems, leading to profitable results.
 - Five interesting and useful insights were found through Exploratory Data Analysis (EDA).

 We also managed to deliver tables with in-depth financial results, as well as buy and sell suggestion tables. All this information can be filtered by using the [House Rocket Cloud App](https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/), that also has the five business insights and a interactive Buy Suggestion Map.   
 
# 9. **Next Steps**
<p align="justify"> Further on, this solution could be improved by a few strategies:
 - Using <a href="https://www.imsl.com/blog/what-is-regression-model">ARIMA</a> to predict the amount of customers over the next six weeks, so that the customers column could be added to the final model.  d. Another interesting study would be to produce a market research, so that data about clients could be collected. Then, a <a href="https://machinelearningmastery.com/clustering-algorithms-with-python/">clustering algorithm</a> </p>
 - Tune even more the regression algorithm, by applying a Bayesian Optimization for instance.
 - Try other regression algorithms to predict the sales for each store.
 - Use different models for the stores on which it's more difficult (higher MAE and MAPE) to predict the sales

# Contact

- brunodifranco99@gmail.com
- [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/BrunoDiFrancoAlbuquerque/)
