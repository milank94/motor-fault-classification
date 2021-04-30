# Data Aquisition

## Description

>This module reads in raw data from Kaggle via the Kagge API and returns a dataframe ready for preprocessing and EDA.

## Kaggle.json 

>You need to create API credentials — it is pretty straightforward. On your Kaggle account, under API, select “Create New API Token,” and kaggle.json will be downloaded on your computer. 
Go to directory — “C:\Users\<username>\.kaggle\” — and paste the downloaded JSON file in this directory.
The `kaggle.json` file in this directory is a placeholder and is empty.


## Usage

>The `load_data` function of `main.py` returns a pd.DataFrame ready for preprocessing and EDA.