
<img width="1115" height="621" alt="image_2026-04-03_16-32-23" src="https://github.com/user-attachments/assets/80220283-5f21-4fa3-b8c0-d45cd7febb59" />

<img width="1118" height="627" alt="image_2026-04-03_16-35-29" src="https://github.com/user-attachments/assets/7f8bd4f9-557f-4c00-93e9-685c06ebdc96" />

# 📊 Telco Churn Strategy: Financial Forecasting & Star Schema

## Project Objective
Reduce telecom customer churn and quantify revenue retention opportunities through a scalable analytics solution. The project combines SQL-based star schema modeling with an interactive Power BI simulator to translate churn reduction into financial impact.

## Business Impact
- Current churn rate: 26.54% → Monthly loss: £139.13K
- Simulated reduction scenario → Potential savings: ~£70K/month
- Key risk segments identified:
  - Month-to-month contracts
  - Electronic check users
  - New customers (<6 months tenure)

---

## Data Architecture
Raw data was transformed into a **Star Schema** using SQL to ensure performance, scalability, and clean analytical modeling.

### Schema Design
- `fact_churn` — Behavioral and financial metrics (tenure, contract type, charges, churn flag)
- `dim_customers` — Customer demographics
- `dim_services` — Service adoption across product offerings

This design enables efficient aggregations and fast Power BI reporting.

---

## Feature Engineering & Insights
Custom business logic was applied to uncover actionable churn drivers:

- **Safety Package Segment**  
  High-retention users subscribed to bundled security services

- **High-Risk New Customers**  
  Early-tenure, month-to-month users with elevated churn probability

- **Payment Friction Analysis**  
  Electronic check users show significantly higher churn vs automated payments

---

## Churn Mitigation Simulator (Power BI)
An interactive **What-If simulation tool** for decision-making.

### Core Features
- Baseline churn and revenue loss tracking
- Adjustable target churn rate (What-If parameter)
- Automatic calculation of required reduction %
- Estimated revenue recovery (monthly savings)
- Residual churn risk after mitigation

---

## Tech Stack
- **SQL** — Data modeling, Star Schema design  
- **Python (Pandas)** — ETL and data preparation  
- **SQLite** — Lightweight data storage  
- **Power BI (DAX)** — Analytical modeling and simulation  

---

## Repository Structure
- `Telco_Churn_Strategy.pbix` — Interactive dashboard  
- `db_creation.py` — Data ingestion pipeline  
- `run_sql.py` — Transformation execution  
- `transformations.sql` — Star Schema logic  
- `dashboard_preview.png` — Dashboard snapshot  
