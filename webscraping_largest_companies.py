{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b301fda7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Rank                Name                   Industry Revenue(USD millions)  \\\n",
      "0    1             Walmart                     Retail               611,289   \n",
      "1    2              Amazon  Retail andcloud computing               513,983   \n",
      "2    3          ExxonMobil         Petroleum industry               413,680   \n",
      "3    4               Apple       Electronics industry               394,328   \n",
      "4    5  UnitedHealth Group                 Healthcare               324,162   \n",
      "\n",
      "  Revenue growth  Employees           Headquarters  \n",
      "0           6.7%  2,100,000  Bentonville, Arkansas  \n",
      "1           9.4%  1,540,000    Seattle, Washington  \n",
      "2          44.8%     62,000          Spring, Texas  \n",
      "3           7.8%    164,000  Cupertino, California  \n",
      "4          12.7%    400,000  Minnetonka, Minnesota  \n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "\n",
    "# The URL of the page you want to scrape\n",
    "url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'\n",
    "\n",
    "# Perform the HTTP request to get the webpage content\n",
    "response = requests.get(url)\n",
    "\n",
    "# Raise an exception if the request failed\n",
    "response.raise_for_status()\n",
    "\n",
    "# Parse the HTML content using BeautifulSoup\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n",
    "# Find the table you want to scrape, Wikipedia tables usually have the 'wikitable' class\n",
    "table = soup.find('table', {'class': 'wikitable'})\n",
    "\n",
    "# Check if a table is found\n",
    "if table:\n",
    "    # Extract the header names\n",
    "    headers = [header.get_text(strip=True) for header in table.find_all('th')]\n",
    "\n",
    "    # Extract the table rows, skipping the header\n",
    "    rows = table.find_all('tr')[1:]\n",
    "\n",
    "    # Extract the table data\n",
    "    table_data = []\n",
    "    for row in rows:\n",
    "        cols = row.find_all(['td', 'th'])  # This gets all table data and header cells\n",
    "        row_data = [ele.get_text(strip=True) for ele in cols]\n",
    "        table_data.append(row_data)\n",
    "\n",
    "    # Create the DataFrame using the header and rows\n",
    "    df = pd.DataFrame(table_data, columns=headers)\n",
    "\n",
    "    # Now you have a DataFrame `df` that you can use for analysis\n",
    "    print(df.head())\n",
    "else:\n",
    "    print(\"No wikitable found on the page.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdb80964",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
