import pandas as pd
import numpy as np
import streamlit as st
from data_clean import cleaned_data
import datetime

#st.write(cleaned_data[:4])
#st.write(cleaned_data[-4:])
#st.slider("Dates",parse_dates(22/01/2020),parse_dates(06/05/2020))
#st.map(cleaned_data)


'''each_dict={}
each_dict_confirmed={}
each_dict_deaths={}
each_dict_recovered={}
for i in countries:
	each_dict[i]=0
	each_dict_confirmed[i]=0
	each_dict_deaths[i]=0
	each_dict_recovered[i]=0

for j in countries:
	if(j in each_dict):
		each_dict_recovered[j]=each_dict_recovered[j]+cleaned_data["recovered"]
	if(j in each_dict):
		each_dict_confirmed[j]=each_dict_confirmed[j]+cleaned_data["confirmed"]
	if(j in each_dict):
		each_dict_deaths[j]=each_dict_deaths[j]+cleaned_data["deaths"]'''


country_list=cleaned_data.country.unique()
time_list=cleaned_data.observationdate.unique()
latitude_list=cleaned_data.latitude.unique()
longitude_list=cleaned_data.longitude.unique()


print(time_list[0])
print(type(time_list[0]))
#d=datetime.date(time_list[0])
#print(d)
