# Text files and CSV

## Pandas
* Data in tabular form? Use [Pandas](https://pandas.pydata.org/) package
* It can easily read and write text/ascii/csv files
* Data is messy? Read the messy data and clean in Pandas
* Pandas can deal with column renaming, missing values, column datatypes, date and time settings and timezones 
* Want to plot all numerical columns in the same axis? Pandas plotting method got you covered
* Pandas documentation [page](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) has a 10 min guide to get you started

### Exercise
We will use Pandas to do the following tasks
* Read rainfall data (accessible from data/ directory) for 36 subdivisions in India
* plot summer monsoon rainfall for all divisions for a given year
* tidy the data and index it by date
* plot time series for selected subdivisions

Data used here is provided by India Meteorological Department(IMD), Govt. of India
and downloaded from [here](https://www.kaggle.com/rajanand/rainfall-in-india) 

import pandas as pd
import matplotlib.pyplot as plt

# read the data
df = pd.read_csv('data/rainfall_in_india_1901-2015.csv',na_values='nan')

# display first 5 rows
df.head()

# display last 5 rows
df.tail()

# prints info of row and column types
# and the number of non-null values
df.info()

# get the number of null values
df.loc[:,'YEAR':'DEC'].isnull().sum()

# unique values in a column
df['SUBDIVISION'].unique()

# index by year
df_year = df.set_index('YEAR')
df_year.head(10)

# cell magic command to get plots inline
%matplotlib inline 
# select a year and plot rainfall through jun-sep for all subdivision
df_year.loc[2003,['SUBDIVISION','Jun-Sep']].plot(x='SUBDIVISION',kind='bar',figsize=(12,4))

# function to convert datetime from strings to python recognized type for datetime
def tidy(df):
    df = df.copy()
    df['date'] = pd.to_datetime(df['year'].astype(str)+df['month'].astype(str),format='%Y%b')
    return df.set_index('date')

# reorient the data so that dates become the index and 
# drop the columns to the right of "ANNUAL" column
df_clean= (df.loc[:,'SUBDIVISION':'DEC']
           .dropna(how='any')
          .set_index(['SUBDIVISION','YEAR'])
          .stack()
          .reset_index()
          .rename(columns={'YEAR':'year','level_2':'month',0:'precip','SUBDIVISION':'subdivision'})
          .reindex(columns=['subdivision','year','month','precip'])
          .pipe(tidy) # calls function tidy with preceeding dataframe as argument
          .drop(columns=['year','month'])
         )
df_clean.tail()

# select data for Kerala and plot
df_krl = df_clean.loc[df_clean['subdivision']=='KERALA',['precip']]
df_krl.loc['1990':'2015'].plot(figsize=(21,3))
plt.suptitle("Monthly rainfall in Kerala",fontweight='bold')

# select rainfall for Telangana state and join it to the dataframe for Kerala
df_tel = df_clean.loc[df_clean['subdivision']=='TELANGANA',['precip']]
df_join = df_tel.join(df_krl,lsuffix='_telangana',rsuffix='_kerala')
df_join.head()

df_join.plot(kind='box')
plt.suptitle("Rainfall distribution",fontweight='bold')

# groupby subdivisions and plot rainall time series for three selected subdivisions
selected_subd = ['KERALA','ARUNACHAL PRADESH','ASSAM & MEGHALAYA']
(df_clean.loc[df_clean['subdivision'].isin(selected_subd)]
         .groupby('subdivision').plot(figsize=(12,4),xlim=('1990','2010')))

## Further references:
* Definitely checout Pandas documentation [page](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html).
* A course of basic Pandas can be found in the [realpython](https://realpython.com/courses/pandas-dataframes-101/) website.
* Also checkout [tomaugspurger](https://tomaugspurger.github.io/modern-1-intro.html) blog on Modern Pandas

