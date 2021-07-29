import pandas as pd
import re

INPUT_CSV_FILE = './data/refined_data.csv' # From OpenRefine
OUTPUT_CSV_FILE = './data/cleaned_data.csv'

# @BEGIN Python_FixSemanticErrorsAndDropInvalidRecords
# @IN input_csv_file @URI file:./data/refined_data.csv
# @OUT cleaned_data @URI file:./data/cleaned_data.csv

# @BEGIN read_csv_file
# @IN input_csv_file @URI file:./data/refined_data.csv
# @OUT raw_data
print("\n\nStep 1: Reading input CSV")
print("-------------------------------------------")
raw_data = pd.read_csv(INPUT_CSV_FILE)
print(raw_data.head())
# @END read_csv_file


# @BEGIN rename_columns
# @IN raw_data
# @OUT preprocessing_data @AS renamed_data
print("\n\nStep 2: Renaming data")
print("-------------------------------------------")
column_names = {"Salary": "Salary_Local"}
preprocessing_data = raw_data.rename(columns=column_names)
print("Data columns renamed:")
for key in column_names.keys():
    print("{} => {}".format(key, column_names[key]))
# @END rename_columns


# @BEGIN drop_records_with_null_values
# @IN renamed_data
# @OUT raw_data @AS not_null_data
print("\n\nStep 3: Dropping records with NULL values")
print("-------------------------------------------")
before_drops = len(preprocessing_data)
print("Number of records dropped for each column:")

for column in preprocessing_data.columns:
    before = len(preprocessing_data)
    preprocessing_data = preprocessing_data[preprocessing_data[column].notna()]
    n_dropped = before - len(preprocessing_data)
    print("{} - {}".format(column, n_dropped))

print("Total: {} records".format(before_drops - len(preprocessing_data)))
# @END drop_records_with_null_values


def parse_range(rnge):
    return [int(s) for s in re.split('\sor\s|\s-\s|-|\s', rnge) if s.isdigit()]

print("\n\nStep 4: Dropping records with invalid age based on experience")
print("-------------------------------------------")
# @BEGIN extract_floor_age
# @IN not_null_data
# @OUT not_null_data @AS not_null_data_with_floor_age
preprocessing_data['floor_age'] = preprocessing_data['Age'].apply(lambda age_range: parse_range(age_range)[0])
# @END extract_floor_age

# @BEGIN extract_floor_experience
# @IN not_null_data_with_floor_age
# @OUT not_null_data @AS not_null_data_with_floor_age_and_experience
preprocessing_data['floor_experience'] = preprocessing_data['Experience'].apply(lambda exp_range: parse_range(exp_range)[0])
# @END extract_floor_experience

# @BEGIN filter_out_invalid_records_based_on_age_and_experience
# @IN not_null_data_with_floor_age_and_experience
# @OUT filtered_data
filtered_data = preprocessing_data[preprocessing_data["floor_age"] > preprocessing_data["floor_experience"]]
# @END filter_out_invalid_records_based_on_age_and_experience

print("BEFORE removing invalid Age: {} records".format(len(preprocessing_data)))
print("AFTER removing invalid Age: {} records".format(len(filtered_data)))


# @BEGIN remove_records_with_undetermined_currency
# @IN filtered_data
# @OUT filtered_data @AS filtered_data_without_undetermined_currency
print("\n\nStep 5: Removing undetermined currencies")
print("-------------------------------------------")
print("BEFORE removing undetermined currency: {} records".format(len(filtered_data)))
filtered_data = filtered_data[filtered_data["Currency"] != "Other"]
print("AFTER removing undetermined currency: {} records".format(len(filtered_data)))
# @END remove_records_with_undetermined_currency

# @BEGIN convert_salaries_to_usd
# @PARAM usd_conversion_rates
# @IN filtered_data_without_undetermined_currency
# @OUT filtered_data @AS usd_salaries_data
print("\n\nStep 6: Converting salaries to USD")
print("-------------------------------------------")
usd_conversion_rates = {
    "USD": 1,
    "GBP": 1.37,
    "CAD": 0.80,
    "EUR": 1.18,
    "SEK": 0.12,
    "AUD/NZD": 0.74,
    "JPY": 0.0091,
    "CHF": 1.09,
    "HKD": 0.13,
    "ZAR": 0.067
}
print("View currencies:")
print(filtered_data["Currency"].unique())
filtered_data["Salary_USD"] = filtered_data.apply(lambda row: usd_conversion_rates[row["Currency"]] * float(row["Salary_Local"]), axis=1)
# @END convert_salaries_to_usd

# @BEGIN export_clean_data
# @IN usd_salaries_data
# @OUT cleaned_data @URI file:./data/cleaned_data.csv
print("\n\nStep 7: Exporting Cleaned Data")
print("-------------------------------------------")
cleaned_data = filtered_data[[
    "Timestamp",
    "Age",
    "Location",
    "Industry",
    "Job_Title",
    "Experience",
    "Salary_USD",
    "Salary_Local",
    "Currency"
]]

print(cleaned_data)
cleaned_data.to_csv(OUTPUT_CSV_FILE, index=False)

# @END convert_salaries_to_usd

print("\n[DONE] Data exported to {}".format(OUTPUT_CSV_FILE))
# @END Python_FixSemanticErrorsAndDropInvalidRecords
