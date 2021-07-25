# Output extracted YW commands found in the file
java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  extract \
  ./clean.py \
  -config extract.listfile

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
  ./clean.py | dot -Tpng -o ./provenance/clean_salaries_combined_view.png && \
  open ./provenance/clean_salaries_combined_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=data \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./clean.py | dot -Tpng -o ./provenance/clean_salaries_process_view.png && \
  open ./provenance/clean_salaries_process_view.png

java -jar ./bin/yesworkflow-0.2.0-jar-with-dependencies.jar \
  graph \
  -config graph.view=process \
  -config graph.workflowbox=show \
  -config graph.layout=TB \
  ./clean.py | dot -Tpng -o ./provenance/clean_salaries_data_view.png && \
  open ./provenance/clean_salaries_data_view.png
