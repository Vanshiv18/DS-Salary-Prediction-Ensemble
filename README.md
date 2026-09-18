💼 Salary Prediction & Analysis
An end-to-end Machine Learning and Business Analytics project that explores salary patterns and provides an interactive salary prediction experience through a deployed Streamlit web application.
🚀 Live Application
🔗 Open the Salary Prediction App
> Enter the relevant employee/job attributes in the application to generate an estimated salary prediction. Results are model-based estimates and should not be treated as guaranteed compensation.
---
📌 Project Overview
This project combines exploratory data analysis, feature preprocessing, machine learning, and interactive deployment to study salary-related patterns.
The project is designed to help users:
Explore salary distributions and patterns.
Understand relationships between available job and employee attributes.
Compare machine learning regression models.
Generate an estimated salary through an interactive interface.
Present analytical findings in a user-friendly web application.
---
🎯 Key Objectives
Perform data cleaning and preprocessing.
Explore salary trends using descriptive statistics and visual analysis.
Prepare numerical and categorical features for machine learning.
Train and compare ensemble regression models.
Evaluate models using regression performance metrics.
Deploy the prediction interface using Streamlit.
---
🧠 Machine Learning Workflow
```text
Raw Dataset
    ↓
Data Loading
    ↓
Data Cleaning & Preprocessing
    ↓
Exploratory Data Analysis
    ↓
Feature Transformation
    ↓
Train–Test Split
    ↓
Regression Model Training
    ↓
Model Evaluation
    ↓
Interactive Streamlit Prediction App
```
Models Used
The deployed application includes a comparison of:
Random Forest Regressor
Gradient Boosting Regressor
The models are evaluated using:
R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
The application uses the model with the stronger evaluation result for the interactive prediction workflow.
> Model performance is calculated when the Streamlit application runs. Metrics should be interpreted in the context of the dataset and train–test split.
---
📊 Analytical Components
The project includes analysis related to:
Salary distribution
Numerical feature relationships
Categorical feature patterns
Data preprocessing and missing-value handling
Model comparison
Salary prediction based on user inputs
Suggested visual assets can be added to the `images/` folder:
```text
images/
├── salary_distribution.png
├── correlation_heatmap.png
├── model_comparison.png
└── prediction_interface.png
```
---
🛠️ Technology Stack
Category	Tools
Programming Language	Python
Data Analysis	Pandas, NumPy
Machine Learning	Scikit-learn
Visualization	Matplotlib / Seaborn, where applicable
Web Application	Streamlit
Dataset Format	Excel (.xlsx)
Deployment	Streamlit Community Cloud
Development Environment	Jupyter Notebook
---
📁 Repository Structure
```text
DS-Salary-Prediction-Ensemble/
│
├── app.py
├── requirements.txt
├── DS_Salary_Analysis_Dataset.xlsx
├── SalaryPredict1.ipynb
├── README.md
└── images/
    └── project screenshots and visualizations
```
---
▶️ Run the Project Locally
1. Clone the repository
```bash
git clone https://github.com/Vanshiv18/DS-Salary-Prediction-Ensemble.git
cd DS-Salary-Prediction-Ensemble
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Launch the Streamlit application
```bash
streamlit run app.py
```
The application will open in your browser at the local Streamlit address.
---
🌐 Deployment
The application is deployed using Streamlit Community Cloud.
🔗 Live App:  
https://ds-salary-prediction-ensemble-zw4xsi2xstqn9lpyrsqm6n.streamlit.app/
For deployment, ensure that the repository contains:
`app.py`
`requirements.txt`
`DS_Salary_Analysis_Dataset.xlsx`
---
⚠️ Limitations
Predictions depend on the quality and coverage of the dataset.
Model results may change based on the train–test split and available features.
Estimated salaries should be used for analytical exploration, not as a definitive salary offer.
The model does not account for every real-world factor influencing compensation.
---
🔮 Future Improvements
Add model hyperparameter tuning.
Introduce cross-validation.
Add explainable AI methods such as feature importance and SHAP.
Include confidence intervals or prediction ranges.
Add filters for job role, location, experience, and other relevant dimensions.
Improve UI design with interactive charts and downloadable prediction reports.
Track model performance across different data segments.
---
👤 Author
Vanshiv Rana
MBA — Data Science & Artificial Intelligence  
B.Tech — Civil
🔗 GitHub: Vanshiv18
---
⭐ Project Note
If you find this project useful, consider giving the repository a ⭐ on GitHub.
