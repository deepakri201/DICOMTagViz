# Run with 
# streamlit run streamlit_viz.py 
# will open up http://localhost:8502/ - can see the plot! 

import json
import streamlit as st
import hiplot as hip
import pandas as pd 

# read in csv 
df_plot = pd.read_csv("C://Users/deepa/git/DICOMTagViz/data/hiplot_qin_prostate.csv")

exp = hip.Experiment()
exp.colorby = "c"
exp.from_dataframe(df_plot).display_st()
