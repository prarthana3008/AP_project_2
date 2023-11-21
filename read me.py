#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis and Visualization with Consumer Complaints API

# This notebook demonstrates how to fetch data from the Consumer Complaints API, perform basic data analysis, and visualize the results using Python libraries like pandas, matplotlib, and seaborn.

# # API Data Fetching and Preparation

# This section covers how to fetch data from the Consumer Complaints API and prepare it for analysis. It includes the definition of a custom Python class to interact with the API and demonstrates how to retrieve and structure the data.

# # API Data Fetching and Preparation

# In[1]:


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


# # Basic DataFrame Operations

# Here, we demonstrate basic operations with the pandas DataFrame containing our fetched data. This includes displaying the first few rows and summarizing the DataFrame's structure, such as column names and data types.

# In[2]:


import pandas as pd

# Assuming your DataFrame is named df
print(df.head())  # Display the first few rows
print(df.info())  # Summary of the DataFrame


# In[4]:


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


# # Data Visualization

# This section contains examples of various data visualizations. It includes code for creating histograms, bar charts, and correlation heatmaps, which are essential for exploring and understanding the data. These visualizations need to be adapted to specific columns in your DataFrame.

# # DataFrame Analysis

# In this final section, we delve deeper into data analysis. The provided code helps in loading the data, displaying its first few rows, summarizing the DataFrame, and computing descriptive statistics for numerical columns. This is crucial for gaining insights into the nature and distribution of the data.

# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[ ]:




