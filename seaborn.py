# Loading essential libraries
import pandas as pd
import seaborn as sns

# Loading Datasets
xls   = pd.ExcelFile('sales.xls')
sales = pd.read_excel(xls, 'Orders')
sales.head()

# Built in Datasets in Seaborn i.e tips, iris, titanic etc
sns.get_dataset_names()

# Relplot
sns.relplot(x='Sales', y='Profit', data = sales)
sns.relplot(x='Sales', y='Profit', data = sales, hue='Order Priority')
sns.relplot(x='Sales', y='Profit', data = sales, hue='Ship Mode')
sns.relplot(x='Sales', y='Profit', data = sales, hue='Order Priority', style='Ship Mode')
sns.relplot(x='Sales', y='Profit', data = sales, size='Discount')
sns.relplot(x='Sales', y='Profit', data = sales, size='Discount',sizes=(35,200))

# Lineplot
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line')
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', hue='Ship Mode')
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', hue='Ship Mode', style='Product Category')
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', hue='Ship Mode', style='Product Category', ci=None)
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', hue='Ship Mode', col='Product Category', ci=None)
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', ci=None)
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', ci='std')
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', estimator = None)
sns.relplot(x='Order Date', y='Sales', data=sales, kind='line', estimator = sum)