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

1. Combined View [\[view\]](https://github.com/gabrielsandoval/salary_survey/blob/master/provenance/clean_salaries_combined_view.png)

2. Data View [\[view\]](https://github.com/gabrielsandoval/salary_survey/blob/master/provenance/clean_salaries_data_view.png)

3. Process View [\[view\]](https://github.com/gabrielsandoval/salary_survey/blob/master/provenance/clean_salaries_process_view.png)
