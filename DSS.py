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
st.markdown(" <right>  <h1>Please Enter Serial Number </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)
st.markdown(" <right>  <h1>                                     الرجاء إدخال كود الشهادة </h1> </font> </right> </h1> ",
            unsafe_allow_html=True)

SN = st.text_input("",value="",key="SN")

if st.button("Done"):            
 st.write("OK")



df = pd.read_excel(File,'DSS')
df.columns  = [i.replace(' ','_') for i in df1.columns]
df.columns  = [i.upper() for i in df1.columns]
df.dropna(axis=0, inplace=True)

#df['RIG_NO.']  = [i.replace(' ','') for i in df1['RIG_NO.']]
#df['RIG_NO.']  = [i.upper() for i in df1['RIG_NO.']]
#df['JOB_TYPE']  = [i.replace(' ','') for i in df1['JOB_TYPE']]
#df['JOB_TYPE']  = [i.upper() for i in df1['JOB_TYPE']]





#st.dataframe(df1,width=1200)
col1, col2, col3 = st.columns(3)

