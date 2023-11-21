## Data Analysis and Visualization with Consumer Complaints API

This notebook demonstrates how to fetch data from the Consumer Complaints API, perform basic data analysis, and visualize the results using Python libraries like pandas, matplotlib, and seaborn.

# API Data Fetching and Preparation

This section covers how to fetch data from the Consumer Complaints API and prepare it for analysis. It includes the definition of a custom Python class to interact with the API and demonstrates how to retrieve and structure the data.

# API Data Fetching and Preparation


```python
import requests
import pandas as pd

class ConsumerComplaintsAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, params={}):
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the status is 4xx or 5xx
        return response.json()

    def to_dataframe(self, json_data):
        # Adjust this if the JSON structure is different
        return pd.DataFrame(json_data.get('hits', {}).get('hits', []))

# Usage example:
base_url = 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/'
client = ConsumerComplaintsAPIClient(base_url)

# Example params - customize these as needed based on the API's documentation
params = {
    'size': 10  # Limits the number of results returned
}

json_response = client.get_data(params=params)
# The API nests the records under 'hits' -> 'hits', and each actual record is under the '_source' key
df = client.to_dataframe(json_response)

# Since each complaint is nested under the '_source' key, we extract this into a separate DataFrame
df = pd.json_normalize(df['_source'])

print(df.head())
```

                       product complaint_what_happened       date_sent_to_company  \
    0  Bank account or service                          2013-11-18T12:00:00-05:00   
    1          Debt collection                          2014-09-04T12:00:00-05:00   
    2                 Mortgage                          2014-08-28T12:00:00-05:00   
    3              Credit card                          2012-06-15T12:00:00-05:00   
    4  Bank account or service                          2012-06-21T12:00:00-05:00   
    
                                          issue                  sub_product  \
    0                  Deposits and withdrawals             Checking account   
    1                     Communication tactics                I do not know   
    2  Application, originator, mortgage broker  Conventional fixed mortgage   
    3                 Advertising and marketing                         None   
    4     Problems caused by my funds being low             Checking account   
    
      zip_code                           tags  has_narrative complaint_id timely  \
    0    94605                 Older American          False        99999    Yes   
    1    93305                           None          False       999988    Yes   
    2    32818                           None          False       999986    Yes   
    3    98221                 Older American          False        99998    Yes   
    4    19140  Older American, Servicemember          False        99997    Yes   
    
      consumer_consent_provided         company_response submitted_via  \
    0                       N/A  Closed with explanation         Phone   
    1                       N/A                   Closed           Web   
    2                       N/A  Closed with explanation         Phone   
    3                       N/A  Closed with explanation           Web   
    4                       N/A                   Closed   Postal mail   
    
                                    company              date_received state  \
    0                 WELLS FARGO & COMPANY  2012-06-12T12:00:00-05:00    CA   
    1         Kimball, Tirey & St. John LLP  2014-08-25T12:00:00-05:00    CA   
    2                  JPMORGAN CHASE & CO.  2014-08-25T12:00:00-05:00    FL   
    3     CAPITAL ONE FINANCIAL CORPORATION  2012-06-12T12:00:00-05:00    WA   
    4  SANTANDER BANK, NATIONAL ASSOCIATION  2012-06-12T12:00:00-05:00    PA   
    
      consumer_disputed company_public_response  \
    0                No                    None   
    1                No                    None   
    2               Yes                    None   
    3                No                    None   
    4                No                    None   
    
                                   sub_issue  
    0                                   None  
    1  Used obscene/profane/abusive language  
    2                                   None  
    3                                   None  
    4                                   None  


# Basic DataFrame Operations

Here, we demonstrate basic operations with the pandas DataFrame containing our fetched data. This includes displaying the first few rows and summarizing the DataFrame's structure, such as column names and data types.


```python
import pandas as pd

# Assuming your DataFrame is named df
print(df.head())  # Display the first few rows
print(df.info())  # Summary of the DataFrame

```

                       product complaint_what_happened       date_sent_to_company  \
    0  Bank account or service                          2013-11-18T12:00:00-05:00   
    1          Debt collection                          2014-09-04T12:00:00-05:00   
    2                 Mortgage                          2014-08-28T12:00:00-05:00   
    3              Credit card                          2012-06-15T12:00:00-05:00   
    4  Bank account or service                          2012-06-21T12:00:00-05:00   
    
                                          issue                  sub_product  \
    0                  Deposits and withdrawals             Checking account   
    1                     Communication tactics                I do not know   
    2  Application, originator, mortgage broker  Conventional fixed mortgage   
    3                 Advertising and marketing                         None   
    4     Problems caused by my funds being low             Checking account   
    
      zip_code                           tags  has_narrative complaint_id timely  \
    0    94605                 Older American          False        99999    Yes   
    1    93305                           None          False       999988    Yes   
    2    32818                           None          False       999986    Yes   
    3    98221                 Older American          False        99998    Yes   
    4    19140  Older American, Servicemember          False        99997    Yes   
    
      consumer_consent_provided         company_response submitted_via  \
    0                       N/A  Closed with explanation         Phone   
    1                       N/A                   Closed           Web   
    2                       N/A  Closed with explanation         Phone   
    3                       N/A  Closed with explanation           Web   
    4                       N/A                   Closed   Postal mail   
    
                                    company              date_received state  \
    0                 WELLS FARGO & COMPANY  2012-06-12T12:00:00-05:00    CA   
    1         Kimball, Tirey & St. John LLP  2014-08-25T12:00:00-05:00    CA   
    2                  JPMORGAN CHASE & CO.  2014-08-25T12:00:00-05:00    FL   
    3     CAPITAL ONE FINANCIAL CORPORATION  2012-06-12T12:00:00-05:00    WA   
    4  SANTANDER BANK, NATIONAL ASSOCIATION  2012-06-12T12:00:00-05:00    PA   
    
      consumer_disputed company_public_response  \
    0                No                    None   
    1                No                    None   
    2               Yes                    None   
    3                No                    None   
    4                No                    None   
    
                                   sub_issue  
    0                                   None  
    1  Used obscene/profane/abusive language  
    2                                   None  
    3                                   None  
    4                                   None  
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10 entries, 0 to 9
    Data columns (total 19 columns):
     #   Column                     Non-Null Count  Dtype 
    ---  ------                     --------------  ----- 
     0   product                    10 non-null     object
     1   complaint_what_happened    10 non-null     object
     2   date_sent_to_company       10 non-null     object
     3   issue                      10 non-null     object
     4   sub_product                7 non-null      object
     5   zip_code                   10 non-null     object
     6   tags                       4 non-null      object
     7   has_narrative              10 non-null     bool  
     8   complaint_id               10 non-null     object
     9   timely                     10 non-null     object
     10  consumer_consent_provided  10 non-null     object
     11  company_response           10 non-null     object
     12  submitted_via              10 non-null     object
     13  company                    10 non-null     object
     14  date_received              10 non-null     object
     15  state                      10 non-null     object
     16  consumer_disputed          10 non-null     object
     17  company_public_response    0 non-null      object
     18  sub_issue                  3 non-null      object
    dtypes: bool(1), object(18)
    memory usage: 1.5+ KB
    None



```python
import pandas as pd

# Assuming your DataFrame is named 'df'
# Load your data into a DataFrame if you haven't already
# df = pd.read_csv('your_data.csv')  # Replace with your data loading method

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Summary of the DataFrame
print("\nSummary of the DataFrame:")
print(df.info())

# Get descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

```

    First few rows of the DataFrame:
                       product complaint_what_happened       date_sent_to_company  \
    0  Bank account or service                          2013-11-18T12:00:00-05:00   
    1          Debt collection                          2014-09-04T12:00:00-05:00   
    2                 Mortgage                          2014-08-28T12:00:00-05:00   
    3              Credit card                          2012-06-15T12:00:00-05:00   
    4  Bank account or service                          2012-06-21T12:00:00-05:00   
    
                                          issue                  sub_product  \
    0                  Deposits and withdrawals             Checking account   
    1                     Communication tactics                I do not know   
    2  Application, originator, mortgage broker  Conventional fixed mortgage   
    3                 Advertising and marketing                         None   
    4     Problems caused by my funds being low             Checking account   
    
      zip_code                           tags  has_narrative complaint_id timely  \
    0    94605                 Older American          False        99999    Yes   
    1    93305                           None          False       999988    Yes   
    2    32818                           None          False       999986    Yes   
    3    98221                 Older American          False        99998    Yes   
    4    19140  Older American, Servicemember          False        99997    Yes   
    
      consumer_consent_provided         company_response submitted_via  \
    0                       N/A  Closed with explanation         Phone   
    1                       N/A                   Closed           Web   
    2                       N/A  Closed with explanation         Phone   
    3                       N/A  Closed with explanation           Web   
    4                       N/A                   Closed   Postal mail   
    
                                    company              date_received state  \
    0                 WELLS FARGO & COMPANY  2012-06-12T12:00:00-05:00    CA   
    1         Kimball, Tirey & St. John LLP  2014-08-25T12:00:00-05:00    CA   
    2                  JPMORGAN CHASE & CO.  2014-08-25T12:00:00-05:00    FL   
    3     CAPITAL ONE FINANCIAL CORPORATION  2012-06-12T12:00:00-05:00    WA   
    4  SANTANDER BANK, NATIONAL ASSOCIATION  2012-06-12T12:00:00-05:00    PA   
    
      consumer_disputed company_public_response  \
    0                No                    None   
    1                No                    None   
    2               Yes                    None   
    3                No                    None   
    4                No                    None   
    
                                   sub_issue  
    0                                   None  
    1  Used obscene/profane/abusive language  
    2                                   None  
    3                                   None  
    4                                   None  
    
    Summary of the DataFrame:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 10 entries, 0 to 9
    Data columns (total 19 columns):
     #   Column                     Non-Null Count  Dtype 
    ---  ------                     --------------  ----- 
     0   product                    10 non-null     object
     1   complaint_what_happened    10 non-null     object
     2   date_sent_to_company       10 non-null     object
     3   issue                      10 non-null     object
     4   sub_product                7 non-null      object
     5   zip_code                   10 non-null     object
     6   tags                       4 non-null      object
     7   has_narrative              10 non-null     bool  
     8   complaint_id               10 non-null     object
     9   timely                     10 non-null     object
     10  consumer_consent_provided  10 non-null     object
     11  company_response           10 non-null     object
     12  submitted_via              10 non-null     object
     13  company                    10 non-null     object
     14  date_received              10 non-null     object
     15  state                      10 non-null     object
     16  consumer_disputed          10 non-null     object
     17  company_public_response    0 non-null      object
     18  sub_issue                  3 non-null      object
    dtypes: bool(1), object(18)
    memory usage: 1.5+ KB
    None
    
    Descriptive Statistics:
                            product complaint_what_happened  \
    count                        10                      10   
    unique                        5                       1   
    top     Bank account or service                           
    freq                          3                      10   
    
                 date_sent_to_company                     issue       sub_product  \
    count                          10                        10                 7   
    unique                          9                        10                 6   
    top     2014-08-28T12:00:00-05:00  Deposits and withdrawals  Checking account   
    freq                            2                         1                 2   
    
           zip_code            tags has_narrative complaint_id timely  \
    count        10               4            10           10     10   
    unique       10               2             1           10      1   
    top       94605  Older American         False        99999    Yes   
    freq          1               3            10            1     10   
    
           consumer_consent_provided         company_response submitted_via  \
    count                         10                       10            10   
    unique                         1                        4             3   
    top                          N/A  Closed with explanation         Phone   
    freq                          10                        6             4   
    
                  company              date_received state consumer_disputed  \
    count              10                         10    10                10   
    unique              9                          2     8                 2   
    top     EQUIFAX, INC.  2012-06-12T12:00:00-05:00    CA                No   
    freq                2                          5     2                 8   
    
           company_public_response                              sub_issue  
    count                        0                                      3  
    unique                       0                                      3  
    top                        NaN  Used obscene/profane/abusive language  
    freq                       NaN                                      1  


# Data Visualization

This section contains examples of various data visualizations. It includes code for creating histograms, bar charts, and correlation heatmaps, which are essential for exploring and understanding the data. These visualizations need to be adapted to specific columns in your DataFrame.

# DataFrame Analysis

In this final section, we delve deeper into data analysis. The provided code helps in loading the data, displaying its first few rows, summarizing the DataFrame, and computing descriptive statistics for numerical columns. This is crucial for gaining insights into the nature and distribution of the data.


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Count the number of complaints by product
product_counts = df['product'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=product_counts.index, y=product_counts.values)
plt.xticks(rotation=45)
plt.title('Number of Complaints by Product')
plt.ylabel('Number of Complaints')
plt.xlabel('Product')
plt.show()

```


    
![png](output_14_0.png)
    



```python
# Count the types of company responses
response_counts = df['company_response'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=response_counts.index, y=response_counts.values)
plt.xticks(rotation=45)
plt.title('Types of Company Responses')
plt.ylabel('Number of Responses')
plt.xlabel('Response Type')
plt.show()

```


    
![png](output_15_0.png)
    



```python
# Convert 'date_received' to datetime
df['date_received'] = pd.to_datetime(df['date_received'])

# Resampling to get monthly complaint counts
monthly_complaints = df.resample('M', on='date_received').size()

# Plotting
plt.figure(figsize=(12, 6))
monthly_complaints.plot()
plt.title('Monthly Complaints Over Time')
plt.ylabel('Number of Complaints')
plt.xlabel('Month')
plt.show()

```


    
![png](output_16_0.png)
    



```python

```
