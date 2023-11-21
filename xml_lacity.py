{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b8512b92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   row      dr_no            date_rptd             date_occ time_occ area  \\\n",
      "0  NaN        NaN                  NaN                  NaN      NaN  NaN   \n",
      "1  NaN  010304468  2020-01-08T00:00:00  2020-01-08T00:00:00     2230   03   \n",
      "2  NaN  190101086  2020-01-02T00:00:00  2020-01-01T00:00:00     0330   01   \n",
      "3  NaN  200110444  2020-04-14T00:00:00  2020-02-13T00:00:00     1200   01   \n",
      "4  NaN  191501505  2020-01-01T00:00:00  2020-01-01T00:00:00     1730   15   \n",
      "\n",
      "     area_name rpt_dist_no part_1_2 crm_cd  ... status   status_desc crm_cd_1  \\\n",
      "0          NaN         NaN      NaN    NaN  ...    NaN           NaN      NaN   \n",
      "1    Southwest        0377        2    624  ...     AO   Adult Other      624   \n",
      "2      Central        0163        2    624  ...     IC   Invest Cont      624   \n",
      "3      Central        0155        2    845  ...     AA  Adult Arrest      845   \n",
      "4  N Hollywood        1543        2    745  ...     IC   Invest Cont      745   \n",
      "\n",
      "                                  location      lat        lon crm_cd_2  \\\n",
      "0                                      NaN      NaN        NaN      NaN   \n",
      "1  1100 W  39TH                         PL  34.0141  -118.2978      NaN   \n",
      "2   700 S  HILL                         ST  34.0459  -118.2545      NaN   \n",
      "3   200 E  6TH                          ST  34.0448  -118.2474      NaN   \n",
      "4  5400    CORTEEN                      PL  34.1685  -118.4019      998   \n",
      "\n",
      "  cross_street crm_cd_3 crm_cd_4  \n",
      "0          NaN      NaN      NaN  \n",
      "1          NaN      NaN      NaN  \n",
      "2          NaN      NaN      NaN  \n",
      "3          NaN      NaN      NaN  \n",
      "4          NaN      NaN      NaN  \n",
      "\n",
      "[5 rows x 29 columns]\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import xml.etree.ElementTree as ET\n",
    "import pandas as pd\n",
    "\n",
    "class XMLDataParser:\n",
    "    def __init__(self, url):\n",
    "        self.url = url\n",
    "\n",
    "    def fetch_xml(self):\n",
    "        response = requests.get(self.url)\n",
    "        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code\n",
    "        return response.content\n",
    "\n",
    "    def parse_xml_to_df(self, xml_data):\n",
    "        root = ET.fromstring(xml_data)\n",
    "        all_records = []\n",
    "        # Assuming that each 'row' element in the XML contains the data record\n",
    "        for row in root.findall('.//row'):\n",
    "            record = {}\n",
    "            for child in row:\n",
    "                # Create a dictionary item with the 'row' tag names as keys and text content as values\n",
    "                record[child.tag] = child.text\n",
    "            all_records.append(record)\n",
    "        return pd.DataFrame(all_records)\n",
    "\n",
    "# Usage\n",
    "url = 'https://data.lacity.org/api/views/2nrs-mtv8/rows.xml?accessType=DOWNLOAD'\n",
    "parser = XMLDataParser(url)\n",
    "xml_content = parser.fetch_xml()\n",
    "df = parser.parse_xml_to_df(xml_content)\n",
    "\n",
    "# Display the DataFrame\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b99192",
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
