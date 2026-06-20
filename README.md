## PCOS: DATA ANALYSIS AND ML PROJECT
Data Analysis and Machine Learning-based PCOS Prediction using Python, Scikit-Learn and XGBoost.

# Dataset Description
This project explores various clinical and hormonal factors linked with Polycystic Ovary Syndrome (PCOS) using data analysis and machine learning methods. The dataset was cleaned, preprocessed, and analysed to identify significant patterns linked to PCOS. Exploratory data analysis (EDA) was performed to find key relations between symptoms and PCOS occurrence. Multiple machine learning models were then trained and evaluated to predict PCOS. Feature importance analysis was lastly used to identify the strongest predictors of the condition.

- Total Records: 541
- Total Features: 45
- Target Variable: PCOS (Y/N)

# Key Features
- Physical measurements (Height, Weight, BMI)
- Hormonal markers (AMH, FSH, LH, TSH, Beta-HCG)
- Follicular and ultrasound parameters
- Menstrual health indicators
- Clinical symptoms such as Weight Gain, Hair Growth, Skin Darkening, Hair Loss, and Pimples


# Machine Learning Approach
The cleaned dataset was divided into training and testing sets using the usual 80:20 split. The target variable was PCOS (Y/N), while the remaining variables were used as the predictive features.

Three machine learning algorithms were evaluated for their ability to predict PCOS, including:
- Logistic Regression
- XGBoost
- Random Forest

# Model Performance
- Logistic Regression  XX.XX%   
- XGBoost              XX.XX%   
- Random Forest
  
The XGBoost model achieved the best predictive performance and was hence selected for the feature importance analysis.

# Feature Importance Analysis
Feature importance analysis was performed using the XGBoost model to identify the variables contributing most strongly to PCOS prediction.

![Feature Importance](plots/feature_importance.png)

Top predictive variables included:

1. Variable_1
2. Variable_2
3. Variable_3
4. Variable_4
5. Variable_5

# Technologies Used
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost

# Conclusion
This project explored the relationship between clinical, hormonal, and lifestyle factors and the occurrence of PCOS. Through exploratory data analysis and machine learning techniques, several important predictors of PCOS were identified.

The results demonstrate how data-driven approaches can support the understanding of healthcare conditions and assist in predictive analysis.
