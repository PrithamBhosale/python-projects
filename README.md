# Python & Pandas Training Series

A comprehensive, interactive training project designed to help senior data analysts master Python and Pandas for business analytics. This project contains structured Jupyter notebooks covering Python fundamentals through advanced data analysis techniques.

---

## Table of Contents

- [Overview](#overview)
- [Notebooks](#notebooks)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Datasets](#datasets)
- [Technologies](#technologies)

---

## Overview

This training series provides hands-on learning through interactive Jupyter notebooks. The curriculum is organized into two main sections:

1. **Python Fundamentals (Notebooks 01-09)** — Core programming concepts required for data analysis
2. **Pandas Mastery (Notebooks 10-15)** — Data manipulation, visualization, and real-world applications

Each notebook follows a consistent structure with concept explanations, reference code, practice exercises, and challenge questions.

---

## Notebooks

### Python Fundamentals

| # | Notebook | Topic |
|---|----------|-------|
| 01 | `01_python_basics.ipynb` | Variables, data types, and basic operations |
| 02 | `02_strings.ipynb` | String manipulation and formatting |
| 03 | `03_numbers.ipynb` | Numeric operations and math functions |
| 04 | `04_lists.ipynb` | List operations, slicing, and comprehensions |
| 05 | `05_dictionaries.ipynb` | Key-value data structures |
| 06 | `06_conditionals.ipynb` | If/else logic and control flow |
| 07 | `07_loops.ipynb` | For/while loops and iteration |
| 08 | `08_functions.ipynb` | Writing reusable code blocks |
| 09 | `09_file_io.ipynb` | Reading and writing files |

### Pandas and Data Analysis

| # | Notebook | Topic |
|---|----------|-------|
| 10 | `10_series_dataframes.ipynb` | Core Pandas data structures |
| 11 | `11_indexing_groupby.ipynb` | Data selection and aggregation |
| 12 | `12_joins.ipynb` | Merging and combining datasets |
| 13 | `13_data_cleaning.ipynb` | Pre-processing and data quality |
| 14 | `14_visualization.ipynb` | Charts with Matplotlib and Seaborn |
| 15 | `15_capstone_projects.ipynb` | Applied business analytics scenarios |

---

## Project Structure

```
python-projects/
│
├── README.md
│
├── data/
│   ├── TechFlow.csv
│   ├── customers_dirty.csv
│   ├── customers_messy.csv
│   ├── customers_new.csv
│   ├── customers_small.csv
│   ├── customer_regions.csv
│   ├── orders.csv
│   ├── products.csv
│   ├── regions.csv
│   ├── daily_metrics.csv
│   ├── monthly_revenue.csv
│   ├── quarterly_revenue.csv
│   ├── nps_surveys.csv
│   └── support_tickets.tsv
│
└── notebooks/
    ├── 01_python_basics.ipynb
    ├── 02_strings.ipynb
    ├── 03_numbers.ipynb
    ├── 04_lists.ipynb
    ├── 05_dictionaries.ipynb
    ├── 06_conditionals.ipynb
    ├── 07_loops.ipynb
    ├── 08_functions.ipynb
    ├── 09_file_io.ipynb
    ├── 10_series_dataframes.ipynb
    ├── 11_indexing_groupby.ipynb
    ├── 12_joins.ipynb
    ├── 13_data_cleaning.ipynb
    ├── 14_visualization.ipynb
    └── 15_capstone_projects.ipynb
```

---

## Prerequisites

Ensure the following are installed:

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Required Python packages:

```bash
pip install pandas matplotlib seaborn jupyter
```

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/PrithamBhosale/python-projects.git
   cd python-projects
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```

3. Launch Jupyter:
   ```bash
   cd notebooks
   jupyter notebook
   ```

4. Open the notebooks in sequential order, starting with `01_python_basics.ipynb`.

---

## Datasets

The project includes realistic business datasets modeled after a SaaS company:

| Dataset | Description | Format |
|---------|-------------|--------|
| `TechFlow.csv` | Core customer data including demographics, subscription tiers, and health scores | CSV |
| `orders.csv` | Transaction and order history | CSV |
| `products.csv` | Product catalog with pricing | CSV |
| `regions.csv` | Geographic region definitions | CSV |
| `customer_regions.csv` | Customer-region mapping | CSV |
| `daily_metrics.csv` | Time-series performance data | CSV |
| `monthly_revenue.csv` | Aggregated monthly financials | CSV |
| `quarterly_revenue.csv` | Quarterly business summaries | CSV |
| `nps_surveys.csv` | Customer satisfaction survey results | CSV |
| `support_tickets.tsv` | Customer support ticket records | TSV |

Additional datasets (`customers_dirty.csv`, `customers_messy.csv`) are intentionally formatted with data quality issues for use in Notebook 13 (Data Cleaning).

---

## Technologies

- **Python 3.x** — Primary programming language
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization
- **Jupyter Notebooks** — Interactive development environment

---

## License

This project is provided for educational purposes.
