"""
Any config specific to model training step goes here.
"""

from pathlib import Path

# General configuration
MONITOR = 'val_loss'
VAL_SPLIT = 0.2
LSTM_UNITS = 100
OPTIMIZER = 'adam'
EPOCHS = 100

# Multi-class classification
OUTPUT_SIZE = 6
ACTIVATION = 'softmax'
LOSS_FUNCTION = 'sparse_categorical_crossentropy'

# Output data path
OUTPUT_DATA_DIR = Path('./output')
