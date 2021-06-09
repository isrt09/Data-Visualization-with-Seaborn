# Loading essential libraries
import pandas as pd
import seaborn as sns

# Loading Datasets
xls   = pd.ExcelFile('sales.xls')
sales = pd.read_excel(xls, 'Orders')
sales.head()

sales = pd.read_csv('sales.csv')
sales.head()

# Built in Datasets in Seaborn i.e tips, iris, titanic etc
sns.get_dataset_names()
sns.load_dataset('tips')

# Seaborn Version 
sns.__version__

# Seaborn Verion Update or Upgrade
pip install seaborn --upgrade

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

# Barplot
sns.catplot(x="Product Category", y="Sales", data=sales, kind='bar')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='bar', hue='Ship Mode')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='bar', hue='Ship Mode')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='bar', hue='Ship Mode', col='Customer Segment')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='bar', hue='Ship Mode', row='Customer Segment')

# Violinplot
sns.catplot(x='Product Category', y="Shipping Cost", data=sales, kind='violin')
sns.catplot(x='Product Category', y="Shipping Cost", data=sales, kind='violin', hue='Ship Mode')
sns.catplot(x='Product Category', y="Shipping Cost", data=sales, kind='violin', hue='Ship Mode', inner='stick')

# Pointplot
sns.catplot(x="Product Category", y="Sales", data=sales, kind='point')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='point', hue='Ship Mode')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='point', hue='Ship Mode')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='point', hue='Ship Mode', col='Customer Segment')
sns.catplot(x="Product Category", y="Sales", data=sales, kind='point', hue='Ship Mode', row='Customer Segment')

# Jointplot
sns.jointplot('Sales','Profit', data=sales)
sns.jointplot(x='Sales',y='Discount', data=sales)
sns.jointplot(x='Sales',y='Discount', data=sales, kind='hex')
sns.jointplot(x='Sales',y='Discount', data=sales, kind='kde')

# Pairplot
sns.pairplot(sales)
sns.pairplot(sales, hue='Ship Mode')
