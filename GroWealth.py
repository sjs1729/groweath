import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
from scipy import optimize
import math
import time
import plotly.express as px
from urllib.request import urlopen
import json
from shared_functions import *

st.set_page_config(
    page_title="GroWealth Investments       ",
    page_icon="nirvana.ico",
    layout="wide",
)


np.set_printoptions(precision=3)

tday = dt.datetime.today()

st.markdown(
    """
    <style>
    .css-k1vhr4 {
        margin-top: -60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
c_1, c_2 = st.columns((8,4))
c_2.image('growealth-logo_long.png', width=300)

st.write("# Welcome to Growealth Investments! ")

html_text = '<p><strong><span style="font-family: Verdana, Geneva, sans-serif; font-size: 20px;">'
html_text = html_text + '<em><span style="color: rgb(65, 168, 95);">GroWealth Investments</span></em>'
html_text = html_text + '</span></strong> is a <span style="color: rgb(255, 47, 146);">SEBI</span> registered '
html_text = html_text + '<span style="color: rgb(255, 47, 146);">Mutual Fund Distributor</span><span style="color: rgb(243, 121, 52);">'
html_text = html_text + '.&nbsp;</span><span style="color: rgb(0, 0, 0);">With our years of expertise in</span>'
html_text = html_text + '<span style="color: rgb(243, 121, 52);">&nbsp;</span><span style="color: rgb(255, 47, 146);">'
html_text = html_text + 'Financial Products</span><span style="color: rgb(243, 121, 52);">&nbsp;</span>'
html_text = html_text + '<span style="color: rgb(0, 0, 0);">and understanding in</span><span style="color: rgb(243, 121, 52);'
html_text = html_text + '">&nbsp;</span><span style="color: rgb(255, 47, 146);">Data Science</span><span style="color: rgb(243, 121, 52);">'
html_text = html_text + '&nbsp;</span><span style="color: rgb(0, 0, 0);">driven</span><span style="color: rgb(243, 121, 52);">'
html_text = html_text + '&nbsp;</span><span style="color: rgb(255, 47, 146);">Quantitative Models,</span><span style="color: rgb(0, 0, 0);">'
html_text = html_text + ' we help our customers define</span><span style="color: rgb(243, 121, 52);">&nbsp;</span><span style="color: rgb(255, 47, 146);">'
html_text = html_text + 'Financial Goals</span><span style="color: rgb(0, 0, 0);"> and develop </span><span style="color: rgb(255, 47, 146);">'
html_text = html_text + 'Investment Plans</span><span style="color: rgb(0, 0, 0);"> to create </span><span style="color: rgb(255, 47, 146);">'
html_text = html_text + 'Long Term Wealth,</span><span style="color: rgb(0, 0, 0);"> pursuing our mantra - </span>'
html_text = html_text + '<span style="color: rgb(44, 130, 201); font-size: 18px;"></span><span style="color: rgb(4, 51, 255); font-size: 17px;">'
html_text = html_text + '<em>Achieving Financial Nirvana.</em></span></p>'

st.markdown(html_text,unsafe_allow_html=True)


st.markdown('')
st.markdown('')

st.markdown(":red[Have you planned your child's **Higher Education**?]")
st.markdown(":red[Are you worried you won't be able to maintain your standard of living **post-retirement**?]")
st.markdown(":red[Is your insurance policy not adequate to cover any **unforeseen life events** or **medical emergency**?]")
st.markdown(":red[Are you spending too much on your **Taxes**?]")

st.markdown('')
st.markdown(":blue[***Let's GroWealth!!!***]")
st.markdown(":email: [helpdesk@gro-wealth.in](emailto:helpdesk@gro-wealth.in)")




@st.cache_data()
def get_mf_perf():
    df = pd.read_csv('mf_data.csv')
    df['Date'] = df['Date'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))

    df.set_index('Date',inplace=True)

    df_perf = pd.read_csv('revised_mf_perf.csv')
    df_perf.set_index('Scheme_Code', inplace=True)

    df_port_dtl = pd.read_csv('mf_port_detail.csv')

    return df, df_perf, df_port_dtl

@st.cache_data()
def get_schm_mapping_data():
    df_schm_map = pd.read_csv('Scheme_Code_Mapping.csv')
    df_schm_map.set_index('Mint_Scheme',inplace=True)
    return df_schm_map
