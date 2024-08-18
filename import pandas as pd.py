import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('sales_data.csv')

# Data cleaning and preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna()

# Sales trend over time
plt.figure(figsize=(10,6))
sns.lineplot(x='Date', y='Sales', data=df)
plt.title('Sales Trend Over Time')
plt.show()

# Top 5 products by sales
top_products = df.groupby('Product')['Sales'].sum().nlargest(5)
print(top_products)
