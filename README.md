# 🛒 Clean-Extract-Visualize: Retail Data Pipeline & Analytics Suite

### 🔗 [View Interactive Suite on Tableau Public][(https://public.tableau.com/app/profile/amulya.v.murthy)]

## 📌 The Problem
Raw e-commerce data is often fragmented across multiple tables and filled with anomalies. Executives need a high-level view of revenue, but Operations and Marketing teams need granular, actionable insights into shipping friction and customer behavior.

## ⚙️ The Solution
I built a professional-grade data pipeline that automates the transformation of raw CSVs into a **3-Part Analytics Suite**.

### The Workflow:
1.  **SQL (Extract):** Joined relational tables (Customers, Orders, Items) in SQLite to calculate order-level revenue.
2.  **Python OOP (Clean):** Developed a reusable `DataCleaner` class to handle nulls and remove price outliers using the **Interquartile Range (IQR)** method.
3.  **Tableau (Visualize):** Designed three specialized dashboards for different business stakeholders.

---

## 📊 Analytics Gallery


**Logistics & Ops Optimizer** | ![Logistics & Ops Optimizer][(images/Logistics & Operations Optimizer.png)]

**Marketing & Loyalty** | ![Marketing & Loyalty][(images/Marketing & Loyalty.png)]

**Executive Overview** | ![Executive Overview][(images/Strategic Sales & Growth Analytics_ Olist Case Study.png)]


---

## 🛠️ Technical Skillset
* **Languages:** Python (Pandas, NumPy, OOP), SQL (SQLite).
* **BI Tools:** Tableau (Advanced Containers, Dual-Axis, Logarithmic Scaling, Action Filters).
* **Statistical Methods:** IQR Outlier Detection, Pareto Distribution, Trend-line Modeling.

## 🏃 How to Run
1. Clone this repo.
2. Download the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
3. Run `python3 main.py` to generate the `ecommerce_final_tableau.csv`.
