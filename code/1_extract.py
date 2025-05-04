import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
# Step 1: Load and save the salary survey
survey_url = 'https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv'
survey_df = pd.read_csv(survey_url)

# Add a year column using helper function
survey_df['year'] = survey_df['Timestamp'].apply(pl.extract_year_mdy)

# Save to cache
survey_df.to_csv('cache/survey.csv', index=False)

# Step 2: Extract COL (Cost of Living) data for each survey year
unique_years = survey_df['year'].dropna().unique()

for year in unique_years:
    # Load COL table from numbeo
    col_tables = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={int(year)}&displayColumn=0")
    col_df = col_tables[1]  # The correct table is index 1
    col_df['year'] = int(year)
    col_df.to_csv(f"cache/col_{int(year)}.csv", index=False)

# Step 3: Load and cache the US state name/abbreviation data
states_url = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"
states_df = pd.read_csv(states_url)
states_df.to_csv("cache/states.csv", index=False)



