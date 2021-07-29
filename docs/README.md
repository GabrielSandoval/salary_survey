## Overview
Data Cleaning project in Python involving OpenRefine and YesWorkflow for Data Provenance

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
