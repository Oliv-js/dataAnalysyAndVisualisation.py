import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set_style('whitegrid')

# Task 1: Load and Explore the Dataset
try:
    url = 'https://raw.githubusercontent.com/tirthajyoti/Stats-Maths-with-Python/master/data/superstore.csv'
    df = pd.read_csv(url, encoding='latin-1')  # Encoding may be required for some datasets
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    raise

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore dataset structure
print("\nDataset structure:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean missing values in 'Postal Code' by dropping rows
if df['Postal Code'].isnull().sum() > 0:
    print("\nDropping rows with missing 'Postal Code'...")
    df.dropna(subset=['Postal Code'], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Group by 'Category' and compute mean sales
category_sales = df.groupby('Category')['Sales'].mean()
print("\nAverage Sales by Category:")
print(category_sales)

# Identify key findings
max_category = category_sales.idxmax()
print(f"\nThe category with the highest average sales is: {max_category}")

# Task 3: Data Visualization
# Line chart: Sales over time
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_over_time = df.groupby('Order Date')['Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(sales_over_time['Order Date'], sales_over_time['Sales'], color='blue')
plt.title('Total Sales Over Time (2014–2017)')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.show()

# Bar chart: Average sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=df, estimator='mean', ci=None)
plt.title('Average Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Average Sales ($)')
plt.show()

# Histogram: Distribution of profit
plt.figure(figsize=(10, 6))
plt.hist(df['Profit'], bins=20, color='green', edgecolor='black')
plt.title('Distribution of Profit')
plt.xlabel('Profit ($)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Sales vs. Profit
plt.figure(figsize=(10, 6))
plt.scatter(df['Sales'], df['Profit'], alpha=0.5, color='purple')
plt.title('Sales vs. Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.show()
