# DS-Salary-Prediction-Ensemble
# Data Science Salary Prediction using Geo-Clustering and Ensemble Learning

## Overview

This project presents a comprehensive end-to-end machine learning pipeline for analyzing and predicting Data Science salaries. It integrates advanced exploratory data analysis (EDA), inflation-adjusted salary modeling, geographic clustering, and ensemble regression techniques to uncover salary-driving factors and build a high-performance predictive model.

The system leverages real-world compensation logic, feature engineering, and supervised learning to estimate salaries based on professional attributes such as experience level, employment type, job category, company size, remote work ratio, and geographic location.

## Technical Architecture

### 1. Exploratory Data Analysis (EDA)
- Salary distribution analysis (raw & log-transformed)
- Experience vs salary segmentation
- Company size and employment type comparison
- Remote work compensation impact
- Country-level salary benchmarking
- Inflation-adjusted salary trend visualization
- Correlation heatmap analysis

### 2. Feature Engineering
- Log transformation to stabilize variance
- Inflation adjustment modeling (year-based multiplier)
- Country-level salary aggregation
- Geo-clustering using KMeans algorithm
- One-hot encoding for categorical variables

### 3. Geo-Clustering (Unsupervised Learning)
- Country-level average salary computation
- KMeans clustering to segment geographic salary groups
- Integration of cluster labels into supervised model pipeline

### 4. Ensemble Regression Modeling
The following models were implemented and compared:

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

Performance Metrics:
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Cross-validation for robustness

XGBoost demonstrated the highest predictive accuracy, capturing non-linear interactions across salary-driving features.

## Interactive Salary Prediction System

The project includes an interactive user-input module that allows real-time salary prediction based on custom inputs. This simulates a production-ready ML inference pipeline.

## Key Insights

- Experience level is the strongest predictor of salary.
- Geographic segmentation significantly impacts compensation.
- Fully remote roles demonstrate measurable salary premiums.
- Large organizations consistently offer higher compensation bands.
- Ensemble methods outperform traditional regression approaches in capturing complex compensation patterns.


## Technologies Used

- Python
- Pandas & NumPy
- Seaborn & Matplotlib
- Scikit-learn
- XGBoost
- OpenPyXL


## Project Outcome

This project demonstrates practical implementation of data preprocessing, clustering, feature engineering, ensemble modeling, and evaluation within a structured ML workflow. It reflects real-world HR analytics and compensation benchmarking systems used in industry.
