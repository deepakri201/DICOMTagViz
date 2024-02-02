# DICOMTagViz

Initial repo for exploratory work for DICOM parameter visualization for NAMIC Project Week 40. 

DICOMTagViz.ipynb: 
- Select a set of important DICOM tags based on Table 5 in this paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7256138/
- Query for these DICOM tags in QIN-Prostate-Repeatability, ProstateX, and other prostate collection in IDC
- Save the csv in /data/hiplot_qin_prostate.csv 
- Use the [hiplot](https://github.com/facebookresearch/hiplot) package to create an interactive plot in colab
- Do this for T2, DWI and ADC
- Add the development of rules -- detecting localizer, orientations, etc. 

streamlit_viz.py: 
- Use the /data/hiplot_qin_prostate.csv as dataframe
- Set up environment using requirements_streamlit.txt file - TO DO. 
- Use [streamlit](https://streamlit.io/) to create/run app
- Run using: `streamlit run streamlit_viz.py`
- Will open http://localhost:8502/ 
