import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

st.set_page_config(page_title="DS Salary Predictor", page_icon="💼", layout="wide")

st.title("💼 Data Science Salary Prediction")
st.write("Interactive ensemble regression dashboard for salary analysis and estimation.")

DATA_PATH = Path("DS_Salary_Analysis_Dataset.xlsx")

@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

def find_target(columns):
    preferred = ["salary_in_usd", "salary_usd", "salary"]
    for candidate in preferred:
        for col in columns:
            if str(col).lower().strip() == candidate:
                return col
    matches = [col for col in columns if "salary" in str(col).lower()]
    return matches[0] if matches else None

@st.cache_resource
def train_models(df, target):
    data = df.copy()
    data[target] = pd.to_numeric(data[target], errors="coerce")
    data = data.dropna(subset=[target])
    data = data[data[target] > 0]

    X = data.drop(columns=[target])
    y = data[target]

    remove_cols = [
        col for col in X.columns
        if str(col).lower() in {"salary", "salary_in_usd", "salary_usd", "salary_currency"}
    ]
    X = X.drop(columns=remove_cols, errors="ignore")

    cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()

    preprocessor = ColumnTransformer([
        ("numeric", Pipeline([
            ("imputer", SimpleImputer(strategy="median"))
        ]), num_cols),
        ("categorical", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]), cat_cols)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model_specs = {
        "Random Forest": RandomForestRegressor(
            n_estimators=250, random_state=42, n_jobs=-1
        ),
        "Gradient Boosting": GradientBoostingRegressor(random_state=42)
    }

    fitted, metrics = {}, []

    for name, model in model_specs.items():
        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])
        pipeline.fit(X_train, y_train)
        predictions = pipeline.predict(X_test)

        metrics.append({
            "Model": name,
            "R²": r2_score(y_test, predictions),
            "MAE": mean_absolute_error(y_test, predictions),
            "RMSE": mean_squared_error(y_test, predictions) ** 0.5
        })
        fitted[name] = pipeline

    return data, X, cat_cols, num_cols, fitted, pd.DataFrame(metrics)

if not DATA_PATH.exists():
    st.error("Dataset not found. Place DS_Salary_Analysis_Dataset.xlsx in the repository root.")
    st.stop()

raw = load_data()
target = find_target(raw.columns)

if target is None:
    st.error("No salary target column was detected. Rename the target column to salary or salary_in_usd.")
    st.stop()

with st.sidebar:
    st.header("Project Controls")
    st.info(f"Target column: {target}")
    st.caption("Models are trained when the app loads.")

try:
    data, X, cat_cols, num_cols, models, results = train_models(raw, target)

    c1, c2, c3 = st.columns(3)
    c1.metric("Records", f"{len(data):,}")
    c2.metric("Features", f"{X.shape[1]:,}")
    c3.metric("Best R²", f"{results['R²'].max():.3f}")

    st.subheader("📊 Model Performance")
    st.dataframe(
        results.style.format({
            "R²": "{:.3f}",
            "MAE": "{:,.2f}",
            "RMSE": "{:,.2f}"
        }),
        use_container_width=True
    )

    st.subheader("🔮 Salary Prediction")
    st.caption("Enter a profile using the available dataset fields.")

    inputs = {}
    columns = st.columns(3)

    for index, col in enumerate(X.columns):
        with columns[index % 3]:
            if col in cat_cols:
                values = sorted(raw[col].dropna().astype(str).unique().tolist())
                inputs[col] = st.selectbox(
                    str(col), values, key=f"field_{index}"
                ) if values else "Unknown"
            elif col in num_cols:
                values = pd.to_numeric(raw[col], errors="coerce").dropna()
                minimum = float(values.min()) if not values.empty else 0.0
                maximum = float(values.max()) if not values.empty else 1.0
                default = float(values.median()) if not values.empty else 0.0
                if minimum == maximum:
                    maximum = minimum + 1.0
                inputs[col] = st.number_input(
                    str(col),
                    min_value=minimum,
                    max_value=maximum,
                    value=min(max(default, minimum), maximum),
                    key=f"field_{index}"
                )
            else:
                inputs[col] = st.text_input(str(col), key=f"field_{index}")

    if st.button("Predict Salary", type="primary"):
        best_model = results.sort_values("R²", ascending=False).iloc[0]["Model"]
        input_df = pd.DataFrame([inputs], columns=X.columns)
        prediction = models[best_model].predict(input_df)[0]

        st.success(f"Estimated Salary: **{prediction:,.2f}**")
        st.caption(f"Generated using {best_model}. This is an analytical estimate, not a guaranteed offer.")

except Exception as error:
    st.error("The application could not train the models with the current dataset.")
    st.exception(error)
