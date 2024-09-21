from PIL import Image
import numpy as np
import pandas as pd #2
import streamlit as st

import datetime
im = Image.open("DSS_Pic.png")
image= np.array(im)
st.image(image)
st.markdown(" <center>  <h1> Training Certificates Verification </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
from datetime import time

Date=datetime.date.today()
Date=Date.strftime('%d-%m-%Y')
#st.write(Date)
st.markdown(" <right>  <h1>Please Enter Serial Number                                                   الرجاء إدخال كود الشهادة </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

SN = st.text_input("Please Enter Serial Number                                                   الرجاء إدخال كود الشهادة ",value="",key="SN")

if st.button("Done"):            
 st.write("OK")

#Data = {'Reading_No': Reading_No,'Well_Name': Well_Name,'Well_ID':Well_ID,'Registeration_Time':Registeration_Time,'Date':Date,'C.K%': CK,'WHP': WHP,'SEP_Pressure': SEP_Pressure,'SEP_Temperature': SEP_Temperature,'FLP': FLP,'FLT': FLT,'Gas_Rate': Gas_Rate,'Condensate': Condensate,'Water': Water,'GOR': GOR,'API': API,'BS&W': BSW,'CO2 %':CO2,'H2S':H2S,'SAL':Sal,'Remarks':Remarks}
#df0=pd.DataFrame([Data])
#df1=pd.DataFrame([Data])
#df1["Date"]=pd.to_datetime(df1["Date"])
#df1["Date"]=df1.Date.dt.strftime('%d-%m-%Y')
#df1["C.K%"]=df1["C.K%"].astype("str")+ "%"
#df1["BS&W"]=df1["BS&W"].astype("str")+ "%"
#df1["Gas_Rate"]=df1["Gas_Rate"].astype("str")+ " MMSCF/D"
#df1["Water"]=df1["Water"].astype("str")+ " BBL/D"
#df1["Condensate"]=df1["Condensate"].astype("str")+ " BBL/D"
#df1["WHP"]=df1["WHP"].astype("str")+ " Psi"
#df1["SEP_Pressure"]=df1["SEP_Pressure"].astype("str")+ " Psi"
#df1["FLP"]=df1["FLP"].astype("str")+ " Psi"
#df1["SEP_Temperature"]=df1["SEP_Temperature"].astype("str")+ " F"
#df1["FLT"]=df1["FLT"].astype("str")+ " F" 
#df1["API"]=df1["API"].astype("str")+ " Deg"

#df1["CO2 %"]=df1["CO2 %"].astype("str")+ "%"
#df1["H2S"]=df1["H2S"].astype("str")+ " PPM"
#df1["SAL"]=df1["SAL"].astype("str")+ " KPPM"
   
#st.dataframe(df1,width=1200)
col1, col2, col3 = st.columns(3)

