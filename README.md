# Python & Pandas Training Series

A comprehensive, interactive training project designed to help senior data analysts master Python and Pandas for business analytics. This project contains structured Jupyter notebooks covering Python fundamentals through advanced data analysis techniques.

---

## Table of Contents

- [Overview](#overview)
- [Module Breakdown](#module-breakdown)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Datasets](#datasets)
- [Technologies](#technologies)

---

## Overview

This training series provides hands-on learning through interactive Jupyter notebooks. The curriculum is organized into two main sections:

1. **Python Fundamentals (Module 0)** — Core programming concepts required for data analysis
2. **Pandas Mastery (Modules 1-6)** — Data manipulation, visualization, and real-world applications

Each notebook follows a consistent structure with concept explanations, reference code, practice exercises, and challenge questions.

---

## Module Breakdown

### Python Fundamentals

| Module | Topic | Description |
|--------|-------|-------------|
| 0.1 | Python Basics | Variables, data types, and basic operations |
| 0.2 | Strings | String manipulation and formatting |
| 0.3 | Numbers | Numeric operations and math functions |
| 0.4 | Lists | List operations, slicing, and comprehensions |
| 0.5 | Dictionaries | Key-value data structures |
| 0.6 | Conditionals | If/else logic and control flow |
| 0.7 | Loops | For/while loops and iteration |
| 0.8 | Functions | Writing reusable code blocks |
| 0.9 | File I/O | Reading and writing files |

### Pandas and Data Analysis

| Module | Topic | Description |
|--------|-------|-------------|
| 1 | Series & DataFrames | Core Pandas data structures |
| 2 | Indexing & GroupBy | Data selection and aggregation |
| 3 | Joins | Merging and combining datasets |
| 4 | Data Cleaning | Pre-processing and data quality |
| 5 | Visualization | Charts with Matplotlib and Seaborn |
| 6 | Real-World Projects | Applied business analytics scenarios |

---

## Project Structure

```
TechFlow/
├── README.md
├── dataset/
│   ├── TechFlow.csv              # Primary customer dataset
│   ├── customers_dirty.csv       # Dataset with data quality issues
│   ├── customers_messy.csv       # Dataset for cleaning exercises
│   ├── customers_new.csv         # Additional customer records
│   ├── customers_small.csv       # Subset for quick testing
│   ├── customer_regions.csv      # Customer-region mapping
│   ├── orders.csv                # Transaction records
│   ├── products.csv              # Product catalog
│   ├── regions.csv               # Geographic regions
│   ├── daily_metrics.csv         # Daily performance metrics
│   ├── monthly_revenue.csv       # Monthly revenue data
│   ├── quarterly_revenue.csv     # Quarterly summaries
│   ├── nps_surveys.csv           # Net Promoter Score data
│   └── support_tickets.tsv       # Customer support records
│
└── query/
    ├── techflow_module_0.1_python_basics.ipynb
    ├── techflow_module_0.2_strings.ipynb
    ├── techflow_module_0.3_numbers.ipynb
    ├── techflow_module_0.4_lists.ipynb
    ├── techflow_module_0.5_dictionaries.ipynb
    ├── techflow_module_0.6_conditionals.ipynb
    ├── techflow_module_0.7_loops.ipynb
    ├── techflow_module_0.8_functions.ipynb
    ├── techflow_module_0.9_file_io.ipynb
    ├── techflow_module_1_series_dataframes.ipynb
    ├── techflow_module_2_indexing_and_groupby.ipynb
    ├── techflow_module_3_joins.ipynb
    ├── techflow_module_4_cleaning.ipynb
    ├── techflow_module_5_visualization.ipynb
    └── techflow_module_6_projects.ipynb
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
   cd query
   jupyter notebook
   ```

4. Open the notebooks in sequential order, starting with `techflow_module_0.1_python_basics.ipynb`.

---

## Datasets

The project includes realistic business datasets modeled after a SaaS company:

| Dataset | Description | Format |
|---------|-------------|--------|
| TechFlow.csv | Core customer data including demographics, subscription tiers, and health scores | CSV |
| orders.csv | Transaction and order history | CSV |
| products.csv | Product catalog with pricing | CSV |
| regions.csv | Geographic region definitions | CSV |
| daily_metrics.csv | Time-series performance data | CSV |
| monthly_revenue.csv | Aggregated monthly financials | CSV |
| quarterly_revenue.csv | Quarterly business summaries | CSV |
| nps_surveys.csv | Customer satisfaction survey results | CSV |
| support_tickets.tsv | Customer support ticket records | TSV |

Additional datasets (`customers_dirty.csv`, `customers_messy.csv`) are intentionally formatted with data quality issues for use in Module 4 (Data Cleaning).

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
