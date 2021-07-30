# Output extracted YW commands found in the provenance/high_level_workflow.py file
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  extract \
  ./provenance/high_level_workflow.py \
  -config extract.listfile > ./provenance/high_level_workflow.yw

# Output .gv file
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  ./provenance/high_level_workflow.py \
  > ./provenance/clean.gv

# Output .png files for (combined|process|data) high_level_workflow views
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=combined \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./provenance/high_level_workflow.py | dot -Tpng -o ./provenance/High_Level_Cleaning_Workflow_combined_view.png && \
  open ./provenance/High_Level_Cleaning_Workflow_combined_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=data \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./provenance/high_level_workflow.py | dot -Tpng -o ./provenance/High_Level_Cleaning_Workflow_data_view.png && \
  open ./provenance/High_Level_Cleaning_Workflow_data_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=process \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./provenance/high_level_workflow.py | dot -Tpng -o ./provenance/High_Level_Cleaning_Workflow_process_view.png && \
  open ./provenance/High_Level_Cleaning_Workflow_process_view.png

# Output extracted YW commands found in the clean.py file
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  extract \
  ./clean.py \
  -config extract.listfile > ./provenance/clean.yw

# Output .gv file
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  ./clean.py \
  > ./provenance/clean.gv

# Output .png files for (combined|process|data) views
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=combined \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./clean.py | dot -Tpng -o ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_combined_view.png && \
  open ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_combined_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=data \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./clean.py | dot -Tpng -o ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_data_view.png && \
  open ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_data_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=process \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./clean.py | dot -Tpng -o ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_process_view.png && \
  open ./provenance/Python_FixSemanticErrorsAndDropInvalidRecords_process_view.png
