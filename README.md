# SWYNEX – Data Cleaning & Preparation

## Project overview
This project demonstrates basic data cleaning and preparation using Python and pandas.

**Important:** The included `raw_data.csv` is a small practice dataset created for this demonstration. If SWYNEX assigned you a specific dataset, replace this sample with the assigned dataset and rerun the notebook/script before submitting.

## Files
- `raw_data.csv` – original practice dataset containing intentionally inconsistent values.
- `cleaned_data.csv` – cleaned output.
- `data_cleaning.ipynb` – Jupyter Notebook showing the workflow.
- `data_cleaning.py` – Python script that reproduces the cleaning steps.

## Cleaning steps
1. Standardized text by trimming spaces and normalizing capitalization.
2. Converted age and purchase amount to numeric values; invalid entries became missing values.
3. Parsed order dates into a consistent date format.
4. Treated ages outside 0–100 and non-positive purchase amounts as invalid.
5. Removed duplicate customer IDs.
6. Filled missing text values with clear labels and numeric values with the median.
7. Exported the result as `cleaned_data.csv`.

## Run locally
Install pandas:
```bash
pip install pandas
```
Keep `raw_data.csv` and `data_cleaning.py` in the same folder, then run:
```bash
python data_cleaning.py
```
