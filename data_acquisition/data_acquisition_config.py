"""
Any config specific to data acquisition step goes here.
"""

from pathlib import Path
from pyprojroot import here as get_project_root
import glob

INPUT_DATA_DIR = get_project_root() / Path('data_acquisition/data')

NORMAL_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/normal/*.csv')
HORI_MIS_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/horizontal/*.csv')
VERT_MIS_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/vertical/*.csv')
IMBALANCE_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/imbalance/*.csv')
OVERHANG_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/overhang/*.csv')
UNDERHANG_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/underhang/*.csv')

