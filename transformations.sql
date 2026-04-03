-- 1. Create the Customer Dimension
CREATE TABLE dim_customers AS
SELECT 
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents
FROM stg_telco_data;

-- 2. Create the Services Dimension
CREATE TABLE dim_services AS
SELECT 
    customerID,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies
FROM stg_telco_data;

-- 3. Create the Fact Table (The core metrics)
CREATE TABLE fact_churn AS
SELECT 
    customerID,
    tenure,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges,
    Churn
FROM stg_telco_data;