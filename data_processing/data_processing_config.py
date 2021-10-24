"""
Any config specific to data processing step goes here.
"""

from pathlib import Path

DATA_TEST_SIZE = 0.2  # Test sample size
SAMPLE_RATE = 50000  # Data acquisition system processing frequency
RESAMPLE_RATE = 100  # Resample rate used to desample the time-series
DURATION = 5  # Time-series duration in seconds

# Output data path
OUTPUT_DATA_DIR = Path('./checkpoints')
OUTPUT_DATA_FILE = OUTPUT_DATA_DIR / Path('train_test_data.p')
