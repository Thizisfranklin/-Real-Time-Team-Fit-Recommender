import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="SystemFit — Player Fit Recommender", layout="wide")

st.title("⚽ SystemFit — Player Fit Recommendation Tool")

# ---------- DEBUG: show what Streamlit can see ----------
st.subheader("🔍 Debug info (you can hide this later)")
st.write("**Current working directory:**", os.getcwd())
st.write("**Files in this directory:**", os.listdir("."))

# If you put df_fit.csv in a subfolder, also show that:
if os.path.exists("data"):
    st.write("**Files in ./data:**", os.listdir("data"))

# ---------- Try to load df_fit.csv ----------
csv_path = "df_fit.csv"   # change this if it's in a folder

if not os.path.exists(csv_path):
    st.error(f"❌ I cannot find `{csv_path}` in this directory. Check the debug file list above.")
    st.stop()

try:
    df = pd.read_csv(csv_path)
    st.success(f"✅ Loaded df_fit.csv with {len(df)} rows and {len(df.columns)} columns.")
except Exception as e:
    st.error(f"⚠️ Found df_fit.csv but failed to read it: {e}")
    st.stop()

# ------------- your existing app code should continue below -------------
