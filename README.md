<h1 align="center">nome do projeto</h1>

<p align="center">Data Science Full Project</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191957066-c9699023-eb0e-4e20-9508-869ee8038ecf.jpg" alt="drawing" width="750"/>
</p>

# 1. **Rossmann and Business Problem**
<p align="justify"> House Rocket is a real estate company whose business model consists in identifying good deals, so that those properties could be bought for an interesting price and futurely sold for a higher price, therefore the company could turn in a profit. For this particular instance, House Rocket will operate in King County, which includes Seattle. </p>

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
- [Regression Algorithms](https://towardsdatascience.com/7-of-the-most-commonly-used-regression-algorithms-and-how-to-choose-the-right-one-fc3c8890f9e3).
- [Cross-Validation Methods](https://medium.com/@soumyachess1496/cross-validation-in-time-series-566ae4981ce4), [Hyperparameter Optimization](https://towardsdatascience.com/7-hyperparameter-optimization-techniques-every-data-scientist-should-know-12cdebe713da) and [Algorithms Performance Metrics (RMSE, MAE, MAPE, R2)](https://machinelearningmastery.com/regression-metrics-for-machine-learning/#:~:text=There%20are%20three%20error%20metrics,Mean%20Absolute%20Error%20(MAE)).

# 5. **Business Insights**

 - ### 1st - Properties that possess waterfront view are, on average, 212.38% more expensive in comparison to the ones that do not have such feature.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962514-70edbf52-c08b-4aa1-9d46-9db3ebd39eca.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling waterfront view properties, since the profit will be higher in absolut values. 
--- 
- ### 2nd - Properties that do not have a basement are, on average, 27.71% cheaper in comparison to the ones that have such feature.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962495-7f9303a2-8c91-47ab-9940-dc984cc0fbc5.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could look to buy properties without a basement that have the potential to possess one. Therefore these properties can be sold for a lot higher price. 
---
- ### 3rd - Properties with good views are, on average, 1.89 times more expensive than the ones with not so good views
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962502-adfbcb5e-2261-46f3-8d1d-1bb8d2281405.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling properties with good views, since the profit will be higher in absolut values.
---
- ### 4th - Regions bordering Lake Washington produce, on average, 36.23% more profit in comparison to other regions.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/192010463-9a0d6027-c6fa-4b4c-9e49-a539873a6ba2.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling properties around Lake Washington, since the profit will be higher in absolut values.
---
- ### 5th - Properties with the lowest prices (on average) were built from 1941 to 1983.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962508-06aaa6af-a466-4181-8d23-e0e1ca88548f.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket would have higher profits buying and selling properties built from the mid 1980's upwards, as well as the ones built from 1900 to 1940.

# 6. **Financial Results**

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

# 7. **Conclusion**
In this project the two main objectives were accomplished:

 - A feasible solution was found for both business problems, leading to profitable results.
 - Five interesting and useful insights were found through Exploratory Data Analysis (EDA).

 We also managed to deliver tables with in-depth financial results, as well as buy and sell suggestion tables. All this information can be filtered by using the [House Rocket Cloud App](https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/), that also has the five business insights and a interactive Buy Suggestion Map.   
 
# 8. **Next Steps**
<p align="justify"> Further on, this solution could be improved by using <a href="https://www.imsl.com/blog/what-is-regression-model">regression models</a> to determine wheter a property has a good buying price, and for which price it could be bought and sold. Another interesting study would be to produce a market research, so that data about clients could be collected. Then, a <a href="https://machinelearningmastery.com/clustering-algorithms-with-python/">clustering algorithm</a> could be applied to identify what types of property features each group of customers would prefer. </p>

# Contact

- brunodifranco99@gmail.com
- [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/BrunoDiFrancoAlbuquerque/)
