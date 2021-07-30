## Overview

Data Cleaning project in Python involving OpenRefine and YesWorkflow for Data Provenance

DETAILED REPORT: [../team63-final-report.pdf](../team63-final-report.pdf)

### File Structure


```
salary_survey/
|---bin/                                                        # Contains the bash file to run YesWorkflow
|   |   provenance.sh
|   |   yesworkflow-0.2.0-jar-with-dependencies.jar
|---data/                                                       # Contains raw, intermediate, and cleaned data
|   |   Ask_A_Manager_Salary_Survey_2019_(Responses).xlsx
|   |   cleaned_data.csv
|   |   DataLinks.txt
|   |   raw_formatted_data.csv
|   |   refined_data.csv
|---docs/                                                       # Code README and Final Submission (.pdf)
|   |   README.md
|   |   team63-final-report.pdf
|---open_refine/                                                # Contains OpenRefine notes and history (.json)
|   |   clustering_notes.txt
|   |   history.json
|---provenance/                                                 # Contains provenance graph dot files(.gv), workflow (data|process|combined) view graphs (.png), and YW-annotations (.txt)
|   |   clean.gv
|   |   clean.yw
|   |   High_Level_Cleaning_Workflow_combined_view.png
|   |   High_Level_Cleaning_Workflow_data_view.png
|   |   High_Level_Cleaning_Workflow_process_view.png
|   |   high_level_workflow.py
|   |   high_level_workflow.yw
|   |   Python_FixSemanticErrors...combined_view.png
|   |   Python_FixSemanticErrors...data_view.png
|   |   Python_FixSemanticErrors...process_view.png
|---sql_queries/                                                # Contains SQL scripts and intermediary data used to check constraints.
|   |   cleaned_data.db
|   |   queries.txt
|   |   Schema.txt
|   |   u0_age_group.csv
|   |   u1_by_industry.csv
|   |   u1_by_location.csv
|   clean.ipynb                                                 # Python Jupyter notebook for data cleaning task.
|   clean.py                                                    # Python Scripts for data cleaning task.
|   explore.ipynb                                               # Jupyter notebook for Exploratory Data Analysis
|   requirements.txt                                            # Dependencies (libraries)

```

### Development Setup
1. Go to your project directory and download the code
    ```
    $ git clone git@github.com:GabrielSandoval/salary_survey.git
    ```

2. Change to that working directory

    ```
    $ cd salary_survey
    ```

3. Install YesWorkflow on your computer by following instructions [here](https://github.com/yesworkflow-org/yw-prototypes).

4. Install dependencies
    ```
    $ pip install -r requiremnents.txt
    ```

5. To run the data cleanup code, run the command below. For Jupyter Notebook users, open the [clean.ipynb](https://github.com/GabrielSandoval/salary_survey/blob/master/clean.ipynb) file.
    ```
    $ python clean.py
    ```

6. To generate provenance graphs, run the command below. Provenance graphs can be viewed in the [/provenance](https://github.com/GabrielSandoval/salary_survey/tree/master/provenance) folder in this directory.
    ```
    $ bash bin/provenance.sh
    ```

### Provenance Graphs

#### High-level Workflow

1. Combined View

  ![\[view\]](../provenance/High_Level_Cleaning_Workflow_combined_view.png)

2. Data View

  ![\[view\]](../provenance/High_Level_Cleaning_Workflow_data_view.png)

3. Process View

  ![\[view\]](../provenance/High_Level_Cleaning_Workflow_process_view.png)

#### Salary Cleaning Workflow

1. Combined View

  ![\[view\]](../provenance/Python_FixSemanticErrorsAndDropInvalidRecords_combined_view.png)

2. Data View

  ![\[view\]](../provenance/Python_FixSemanticErrorsAndDropInvalidRecords_data_view.png)

3. Process View

  ![\[view\]](../provenance/Python_FixSemanticErrorsAndDropInvalidRecords_process_view.png)
