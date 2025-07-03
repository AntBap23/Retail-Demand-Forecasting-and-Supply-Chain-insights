
# 📦 Retail Demand Forecasting & Supply Chain Insights

An end-to-end data pipeline and analysis framework to optimize retail demand forecasting and inventory replenishment. This project integrates **Python**, **SQL**, and **Power BI** to deliver data-driven procurement recommendations, visual KPIs, and cost-saving insights across regions and product categories.

---

## 🧠 Project Overview

- **Goal**: Reduce inventory carrying costs and improve procurement decisions using real-time data and forecasting.
- **Stack**: Python for data ingestion and validation, SQL for transformation and modeling, Power BI for KPI dashboards.
- **Key Features**:
  - DAX-based EOQ & forecasting models embedded in Power BI
  - SQL views structured as a star-schema for BI consumption
  - Automated data loading and validation from local sources

---

## 📁 Repository Structure

```

retail-demand-forecasting/
│
├── db/                  # SQL schema, table setup, constraints
├── sql/                 # SQL views for BI modeling and metrics
├── validate/            # Data validation logic and test queries
├── visuals/             # 📊 Power BI screenshots and report previews (to be added)
│
├── eda.ipynb            # Exploratory analysis and forecasting prototypes
├── load\_data.py         # Script to load and clean raw data into the database
├── requirements.txt     # Python dependencies
├── .env                 # DB credentials and config variables
├── LICENSE              # License file
└── README.md            # Project documentation

````

---

## ⚙️ Technologies Used

| Layer        | Tools                                     |
|--------------|--------------------------------------------|
| Ingestion    | Python (pandas, psycopg2, SQLAlchemy)      |
| Validation   | SQL queries + pandas assertions            |
| Modeling     | SQL (PostgreSQL), star-schema modeling     |
| BI           | Power BI (DAX formulas, forecasting cards) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AntBap23/retail-demand-forecasting.git
cd retail-demand-forecasting
````

### 2. Set up environment variables

Create a `.env` file in the root directory:

```env
DB_HOST=host
DB_PORT=port
DB_NAME=db
DB_USER=your_user
DB_PASSWORD=your_password
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Load Data

```bash
python load_data.py
```

This will:

* Connect to PostgreSQL
* Load cleaned CSVs into staging tables
* Run validation checks via the `validate/` module

---

## ▶️ How to Use

1. **Run SQL views** from the `sql/` folder to generate fact and dimension tables.
2. **Connect Power BI** to your local or hosted PostgreSQL database.
3. Use the pre-built dashboard to:

   * Monitor forecasted demand vs. actual sales
   * Evaluate reorder points and EOQ recommendations
   * Drill into supplier lead times, SKU performance, and regional breakdowns

---

## 📊 Key Metrics Tracked

| Metric                | Description                                         |
| --------------------- | --------------------------------------------------- |
| EOQ                   | Economic Order Quantity per SKU                     |
| Forecast Accuracy     | Accuracy of DAX or statistical forecast methods     |
| Inventory Turnover    | Efficiency of inventory usage over time             |
| Reorder Flag          | Indicator for low-stock alerts and reorder triggers |
| Cost Savings Estimate | Estimated reduction in carrying costs               |

---

## 🖼 Sample Visuals

Screenshots, report pages, and KPI tiles from the Power BI dashboard will be added to the `visuals/` folder. Examples may include:

* 📉 Forecast vs. Actual Demand by Region
* 🧮 EOQ Recommendations by Product
* 📦 Inventory Turnover Heatmap
* 📍 Supplier Lead Time Comparison

---

## 🔍 Insights & Use Cases

* Identify SKUs with high holding costs and optimize restocking frequency
* Compare supplier performance using lead time visualizations
* Make real-time procurement decisions using scenario filters in Power BI
* Evaluate regional sales patterns to forecast future demand

---

## 🛠 Future Improvements

* Add time-series forecasting models (Prophet, ARIMA) in Python
* Integrate external supplier APIs for lead time updates
* Deploy Power BI dashboard via Power BI Service or embed via Web
* Add unit tests to validate SQL logic and data quality

---

## 📄 License

This project is licensed for academic and portfolio use under the MIT License.

---

## 👤 Author

**Anthony Baptiste**
[LinkedIn](https://www.linkedin.com/in/anthony-baptiste00)
[Portfolio](https://antbap23.github.io/portfolio)



