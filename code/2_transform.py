import pandas as pd
import streamlit as st
import pandaslib as pl

#Load datasets from cache
survey_df = pd.read_csv("cache/survey.csv")
states_df = pd.read_csv("cache/states.csv")

# Load all cost of living (COL) files
col_list = []
for yr in survey_df["year"].dropna().unique():
    year = int(yr)
    col_file = f"cache/col_{year}.csv"
    col_df = pd.read_csv(col_file)
    col_df["year"] = year  # Redundant but consistent
    col_list.append(col_df)

# Combine all COL data into one dataframe
col_combined = pd.concat(col_list, ignore_index=True)

# Clean country data
survey_df["_country"] = survey_df["What country do you work in?"].apply(pl.clean_country_usa)

# Join with state abbreviation codes
merged_states = survey_df.merge(
    states_df,
    how="inner",
    left_on="If you're in the U.S., what state do you work in?",
    right_on="State"
)

# Engineer full city string: "City, ST, Country"
merged_states["_full_city"] = (
    merged_states["What city do you work in?"] + ", " +
    merged_states["Abbreviation"] + ", " +
    merged_states["_country"]
)

# Merge with cost of living data
final_df = merged_states.merge(
    col_combined,
    how="inner",
    left_on=["year", "_full_city"],
    right_on=["year", "City"]
)

# Clean and adjust salary
salary_col = "What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)"
final_df["_annual_salary_cleaned"] = final_df[salary_col].apply(pl.clean_currency)

final_df["_annual_salary_adjusted"] = final_df.apply(
    lambda row: row["_annual_salary_cleaned"] * (100 / row["Cost of Living Index"]),
    axis=1
)

# Save final dataset
final_df.to_csv("cache/survey_dataset.csv", index=False)

# Create pivot reports

# 1. By location and age
pivot_age = final_df.pivot_table(
    index="_full_city",
    columns="How old are you?",
    values="_annual_salary_adjusted",
    aggfunc="mean"
)
pivot_age.to_csv("cache/annual_salary_adjusted_by_location_and_age.csv")

# 2. By location and education
pivot_edu = final_df.pivot_table(
    index="_full_city",
    columns="What is your highest level of education completed?",
    values="_annual_salary_adjusted",
    aggfunc="mean"
)
pivot_edu.to_csv("cache/annual_salary_adjusted_by_location_and_education.csv")
