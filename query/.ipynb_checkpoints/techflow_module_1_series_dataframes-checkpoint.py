"""
================================================================================
TechFlow Data Analysis Course - Module 1: Series and DataFrames Introduction
================================================================================

This module introduces the foundational concepts of pandas:
- NumPy arrays vs Pandas Series
- Pandas Series basics
- Pandas DataFrame basics
- Real-world data manipulation examples

Dataset: TechFlow.csv (B2B SaaS customer data)
================================================================================
"""


# ==============================================================================
# SECTION 1: IMPORTS & SETUP
# ==============================================================================

# Import the essential libraries for data analysis
import numpy as np   # NumPy: For numerical operations and array handling
import pandas as pd  # Pandas: For data manipulation and analysis

# Configure pandas display options for better readability
# These settings ensure we can see enough data without truncation
pd.set_option('display.max_columns', 15)      # Show up to 15 columns
pd.set_option('display.width', 120)           # Console width for display
pd.set_option('display.max_rows', 20)         # Show up to 20 rows
pd.set_option('display.precision', 2)         # 2 decimal places for floats

print("=" * 70)
print("MODULE 1: Series and DataFrames Introduction")
print("=" * 70)
print("\n✓ NumPy and Pandas imported successfully")
print(f"  - NumPy version: {np.__version__}")
print(f"  - Pandas version: {pd.__version__}")
print()


# ==============================================================================
# SECTION 2: LOADING THE DATASET
# ==============================================================================

print("-" * 70)
print("SECTION 2: Loading the TechFlow Dataset")
print("-" * 70)

# Load the CSV file into a pandas DataFrame
# The path is relative to the query folder where this script is located
df = pd.read_csv('../dataset/TechFlow.csv')

# Display the first 5 rows to get a quick look at the data
# .head() is your go-to method for initial data inspection
print("\n▶ First 5 rows of the dataset:")
print(df.head())

# Check the shape of the DataFrame (rows, columns)
# Shape is a tuple: (number_of_rows, number_of_columns)
print(f"\n▶ Dataset Shape: {df.shape}")
print(f"  - Number of rows: {df.shape[0]}")
print(f"  - Number of columns: {df.shape[1]}")

# Display all column names
# Columns are the features/variables in our dataset
print("\n▶ Column Names:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i:2}. {col}")

# Check data types of each column
# Understanding data types is crucial for proper data manipulation
print("\n▶ Data Types:")
print(df.dtypes)
print()


# ==============================================================================
# SECTION 3: NUMPY ARRAYS VS PANDAS SERIES
# ==============================================================================

print("-" * 70)
print("SECTION 3: NumPy Arrays vs Pandas Series")
print("-" * 70)

# Let's use the 'MonthlyRevenue' column to compare NumPy arrays and Pandas Series

# Create a NumPy array from the MonthlyRevenue column
# NumPy arrays are the foundation for numerical computing in Python
revenue_array = np.array(df['MonthlyRevenue'])

# Convert the same column to a Pandas Series
# A Series is a one-dimensional labeled array
revenue_series = pd.Series(df['MonthlyRevenue'])

# Compare the types
print("\n▶ Type Differences:")
print(f"  - NumPy array type:   {type(revenue_array)}")
print(f"  - Pandas Series type: {type(revenue_series)}")

# Key difference: Index behavior
# NumPy arrays use integer position only; Series have labeled indexes
print("\n▶ Index Behavior:")
print(f"  - NumPy array has no explicit index - uses position only")
print(f"  - Pandas Series index: {revenue_series.index.tolist()[:10]} ... (showing first 10)")

# Accessing elements: both support integer indexing
print("\n▶ Accessing the 3rd element (index 2):")
print(f"  - NumPy array[2]:  {revenue_array[2]}")
print(f"  - Pandas Series[2]: {revenue_series[2]}")

# Basic operations work similarly on both
print("\n▶ Basic Operations Comparison:")
print(f"  - NumPy mean:  {np.mean(revenue_array):.2f}")
print(f"  - Series mean: {revenue_series.mean():.2f}")
print(f"  - NumPy sum:   {np.sum(revenue_array)}")
print(f"  - Series sum:  {revenue_series.sum()}")

# Why choose Series over Array?
# Series provide: labels, missing data handling, alignment, and more methods
print("\n▶ Key Takeaway:")
print("  NumPy arrays are great for pure numerical computation.")
print("  Pandas Series add labels, alignment, and richer functionality.")
print()


# ==============================================================================
# SECTION 4: PANDAS SERIES BASICS
# ==============================================================================

print("-" * 70)
print("SECTION 4: Pandas Series Basics")
print("-" * 70)

# Select a single column from a DataFrame to get a Series
# Using bracket notation: df['column_name']
seat_count = df['SeatCount']

# Verify it's a Series
print(f"\n▶ Type of 'seat_count': {type(seat_count)}")

# The INDEX: Every Series has an index (labels for each element)
print("\n▶ Series Index:")
print(f"  Index: {seat_count.index.tolist()}")
print(f"  Index type: {type(seat_count.index)}")

# The VALUES: The actual data stored in the Series
# .values returns a NumPy array of the underlying data
print("\n▶ Series Values (first 10):")
print(f"  {seat_count.values[:10]}")
print(f"  Values type: {type(seat_count.values)}")

# Using .head() to preview the Series
# .head(n) returns the first n elements (default is 5)
print("\n▶ Using .head() to see first 5 seats:")
print(seat_count.head())

# Using .describe() for statistical summary (works on numeric Series)
# This is incredibly useful for quick exploratory data analysis
print("\n▶ Statistical Summary using .describe():")
print(seat_count.describe())

# Let's also look at a non-numeric (categorical) Series
industry = df['Industry']
print("\n▶ Non-numeric Series - Industry:")
print(f"  First 5 values: {industry.head().tolist()}")

# For non-numeric, describe() shows different statistics
print("\n▶ describe() on categorical Series (Industry):")
print(industry.describe())
print()


# ==============================================================================
# SECTION 5: PANDAS DATAFRAME BASICS
# ==============================================================================

print("-" * 70)
print("SECTION 5: Pandas DataFrame Basics")
print("-" * 70)

# A DataFrame is a 2D labeled data structure (like a spreadsheet or SQL table)
# It's essentially a collection of Series sharing the same index

# Selecting multiple columns - returns a new DataFrame
# Pass a list of column names inside brackets
selected_columns = df[['CompanyName', 'Industry', 'MonthlyRevenue', 'SeatCount']]
print("\n▶ Selecting Multiple Columns:")
print(selected_columns.head())

# Row slicing using standard Python slice notation
# This works on the DataFrame's integer position
print("\n▶ Row Slicing (rows 5 to 9):")
print(df[5:10])  # Note: end index is exclusive

# Accessing rows using .iloc (integer-location based indexing)
# .iloc[row_index] returns a Series (the row as a Series)
print("\n▶ Accessing Row 0 using iloc:")
print(df.iloc[0])

# .iloc can also select specific rows and columns
# df.iloc[row_index, column_index] or df.iloc[rows, columns]
print("\n▶ Accessing rows 0-2, columns 0-4 using iloc:")
print(df.iloc[0:3, 0:5])

# Accessing single column using bracket notation
# df['column'] returns a Series
print("\n▶ Single Column Access using bracket notation:")
print(df['CompanyName'].head())

# You can also use dot notation for column access (if column name is valid Python identifier)
# df.CompanyName is equivalent to df['CompanyName']
print("\n▶ Same column using dot notation:")
print(df.CompanyName.head())

# Accessing a single cell using iloc
# df.iloc[row, column] returns a single value
print("\n▶ Accessing single cell - row 3, column 1 (CompanyName):")
print(f"  Value: {df.iloc[3, 1]}")

# Using .loc for label-based access (using row index and column names)
print("\n▶ Using .loc with labels - row 3, 'CompanyName' column:")
print(f"  Value: {df.loc[3, 'CompanyName']}")
print()


# ==============================================================================
# SECTION 6: REAL-WORLD MINI EXAMPLES
# ==============================================================================

print("-" * 70)
print("SECTION 6: Real-World Mini Examples with TechFlow Data")
print("-" * 70)

# ---------- Example 1: Counting Unique Values ----------
# How many unique industries are represented in our customer base?
print("\n▶ Example 1: Counting Unique Values")
print("  Question: How many unique industries do our customers represent?")

unique_industries = df['Industry'].nunique()
print(f"\n  Number of unique industries: {unique_industries}")

# Let's see what they are and how many customers are in each
print("\n  Breakdown by industry:")
print(df['Industry'].value_counts())


# ---------- Example 2: Finding Average of a Numeric Column ----------
# What is the average Monthly Revenue and Seat Count across all customers?
print("\n" + "-" * 40)
print("\n▶ Example 2: Finding Averages of Numeric Columns")
print("  Question: What are the average revenue and seat metrics?")

avg_revenue = df['MonthlyRevenue'].mean()
avg_seats = df['SeatCount'].mean()
total_revenue = df['MonthlyRevenue'].sum()

print(f"\n  Average Monthly Revenue: ${avg_revenue:,.2f}")
print(f"  Average Seat Count: {avg_seats:.1f}")
print(f"  Total Monthly Revenue: ${total_revenue:,.2f}")


# ---------- Example 3: Boolean Comparisons and Filtering ----------
# How many customers have churned (Cancelled = 1)?
print("\n" + "-" * 40)
print("\n▶ Example 3: Boolean Comparison and Filtering")
print("  Question: How many customers have cancelled their subscription?")

# Boolean comparison creates a Series of True/False values
is_cancelled = df['Cancelled'] == 1
print(f"\n  Boolean Series (first 10): {is_cancelled.head(10).tolist()}")

# Count True values using .sum() (True = 1, False = 0)
cancelled_count = is_cancelled.sum()
active_count = (df['Cancelled'] == 0).sum()
churn_rate = (cancelled_count / len(df)) * 100

print(f"\n  Cancelled customers: {cancelled_count}")
print(f"  Active customers: {active_count}")
print(f"  Churn rate: {churn_rate:.1f}%")

# Filter DataFrame to show only cancelled customers
print("\n  Cancelled customers (Company Names):")
cancelled_companies = df[is_cancelled]['CompanyName'].tolist()
for company in cancelled_companies[:5]:  # Show first 5
    print(f"    - {company}")
if len(cancelled_companies) > 5:
    print(f"    ... and {len(cancelled_companies) - 5} more")
print()


# ==============================================================================
# SECTION 7: FINAL SUMMARY
# ==============================================================================

print("=" * 70)
print("FINAL SUMMARY: Key Concepts from Module 1")
print("=" * 70)

summary = """
▶ WHAT IS A SERIES?
  A Pandas Series is a one-dimensional labeled array.
  Think of it as a single column from a spreadsheet.
  
  Key characteristics:
  • Has an index (row labels) and values (the actual data)
  • Can hold any data type (integers, floats, strings, etc.)
  • Supports vectorized operations (apply operations to all elements at once)
  • Created from: df['column_name'] or pd.Series(data)

▶ WHAT IS A DATAFRAME?
  A Pandas DataFrame is a two-dimensional labeled data structure.
  Think of it as a complete spreadsheet or a SQL table.
  
  Key characteristics:
  • Collection of Series sharing the same index (rows)
  • Each column is a Series with a name (column label)
  • Supports row and column indexing (using .loc, .iloc, or brackets)
  • Created from: pd.read_csv(), dictionaries, or other data structures

▶ WHEN TO USE EACH?

  Use a SERIES when you:
  • Work with a single variable/column
  • Perform operations on one column at a time
  • Need to extract statistics from one feature

  Use a DATAFRAME when you:
  • Work with multiple related variables/columns
  • Need to join, merge, or reshape data
  • Perform analysis across multiple features
  • Load data from files (CSV, Excel, SQL, etc.)

▶ KEY METHODS LEARNED:
  Series:   .head(), .describe(), .values, .index, .mean(), .sum()
  DataFrame: .head(), .shape, .columns, .dtypes, .iloc[], .loc[]
            Column selection: df['col'], df[['col1', 'col2']]
            Row slicing: df[start:end]
"""

print(summary)

print("=" * 70)
print("End of Module 1 - You're ready to move on to Data Exploration!")
print("=" * 70)
