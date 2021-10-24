"""
Any config specific to data acquisition step goes here.
"""

from pathlib import Path
import glob

# Select input data directory
INPUT_DATA_DIR = Path('./data_acquisition/data')

# Input data paths
NORMAL_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/normal/*.csv')
HORI_MIS_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/horizontal/*.csv')
VERT_MIS_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/vertical/*.csv')
IMBALANCE_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/imbalance/*.csv')
OVERHANG_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/overhang/*.csv')
UNDERHANG_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/underhang/*.csv')

# Output data path
OUTPUT_DATA_DIR = Path('./checkpoints')
OUTPUT_DATA_FILE = OUTPUT_DATA_DIR / Path('raw_data.p')
