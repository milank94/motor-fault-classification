acquire-data:
	@echo "Downloading data"
	@python data_acquisition/main.py

run-eda:
	@echo "Run EDA"
	@python eda/signal_processing_experiment.py

process-data:
	@echo "Processing data"
	@python data_processing/main.py

train-model:
	@echo "Training model"
	@python model_training/main.py

evaluate-model:
	@echo "Evaluating model"
	@python model_evaluation/model_evaluation.py
