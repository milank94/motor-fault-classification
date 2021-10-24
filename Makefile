acquire-data:
	@echo "Downloading data"
	@python data_acquisition/main.py

process-data:
	@echo "Processing data"
	@python data_processing/main.py
