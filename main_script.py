from imaplib import _Authenticator
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
# auth

data = pd.read_csv("ds.csv")
df = pd.DataFrame(data)
st.write(df)
