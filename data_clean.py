import pandas as pd
import numpy as np
import streamlit as st

MERGED_DATA_URL=("H:/Repository/data science/covid_analysis/merged.csv")


input_data=pd.read_csv(MERGED_DATA_URL,nrows=38)
cleaned_data=input_data.dropna(how="any")

#print(cleaned_data[["observationdate","country"]])


