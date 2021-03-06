# @BEGIN High_Level_Cleaning_Workflow
# @IN raw_salary_survey_responses @URI file:./data/Ask_A_Manager_Salary_Survey_2019_(Responses).csv
# @OUT most_lucrative_industries_chart
# @OUT most_lucrative_locations_chart

# @BEGIN EXCEL_RenameColumnsAndRemoveIrrelevantOnes
# @IN raw_salary_survey_responses @URI file:./data/Ask_A_Manager_Salary_Survey_2019_(Responses).csv
# @OUT raw_formatted_data @URI file:./data/raw_formatted_data.csv
# @END EXCEL_RenameColumnsAndRemoveIrrelevantOnes

# @BEGIN OpenRefine_FixSyntacticIssuesAndClusterValues
# @IN raw_formatted_data @URI file:./data/raw_formatted_data.csv
# @OUT refined_data @URI file:./data/refined_data
# @END OpenRefine_FixSyntacticIssuesAndClusterValues

# @BEGIN Python_FixSemanticErrorsAndDropInvalidRecords
# @IN refined_data @URI file:./data/refined_data.csv
# @OUT cleaned_data @URI file:./data/cleaned_data.csv
# @END Python_FixSemanticErrorsAndDropInvalidRecords

# @BEGIN JupyterNotebook_ExploratoryDataAnalysis
# @IN cleaned_data @URI file:./data/refined_data.csv
# @OUT most_lucrative_industries_chart
# @OUT most_lucrative_locations_chart
# @END JupyterNotebook_ExploratoryDataAnalysis

# @END High_Level_Cleaning_Workflow

