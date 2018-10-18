# Kaggle-House_Prices_Advanced_Regression_Techniques  

* 分析前準備
    0. Exploratory Data Analysis
    1. 資料標準化 
    2. 補空值
        * 機器學習方式 
        * 或是利用所發掘的資料特性來補
        * 或是直接補平均 
* 建模分析 4和5須"調參", 嘗試不同參數，找最適模型)
    * 使用Scikit-learn
        1. Ridge regression
        2. Lasso regression 
        3. ElasticNet regression 
        4. 解釋為何樹演算法可做回歸 
        5. Random Forest regression (畫出feature importance) 
    * 使用XGBoost
        5. Gradient Boosted Tree regression (畫出feature importance) 
* 嘗試有可能讓模型變得更佳的方式
    * 清掉房價是離群值的資料(會影響機器的學習效果)  
    * PCA降維後再做XGBoost 
    * feature engineering 
* 上傳至kaggle看排名。


## Reference
* 參考資料 https://www.kaggle.com/c/house-prices-advanced-regression-techniques/kernels
