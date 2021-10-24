acquire-data:
	@echo "Downloading data"
	@python data_acquisition/main.py

run-eda:
	@echo "Run EDA"
	@python eda/signal_processing_experiment.py

process-data:
	@echo "Processing data"
	@python data_processing/main.py
