"""
Any config specific to data acquisition step goes here.
"""

from pathlib import Path
from pyprojroot import here as get_project_root
import glob


# +
INPUT_DATA_DIR = get_project_root() / Path('data_acquisition/data')

NORMAL_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/normal/*.csv')
HORI_MIS_FILE_NAMES_1 = glob.glob(str(INPUT_DATA_DIR)+'/1.0mm/*.csv')
HORI_MIS_FILE_NAMES_2 = glob.glob(str(INPUT_DATA_DIR)+'/2.0mm/*.csv')
IMBALANCE_FILE_NAMES = glob.glob(str(INPUT_DATA_DIR)+'/25g/*.csv')

COLUMNS = ['encoder', 'x_1', 'y_1', 'z_1', 'x_2', 'y_2', 'z_2', 'noise']
# -

