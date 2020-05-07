import pandas as pd
import numpy as np

COVID_DATA_URL=("H:/Repository/data science/covid_analysis/covid_19_data.csv")
COUNTRY_DATA_URL=("H:/Repository/data science/covid_analysis/countries.csv")

file_out="merged.csv"

covid_data=pd.read_csv(COVID_DATA_URL,nrows=22190)
country_data=pd.read_csv(COUNTRY_DATA_URL,nrows=246)

result_csv=pd.merge(covid_data,country_data,how="left",on=["country"])
result_csv.to_csv(file_out,encoding="utf-8",index=False)

