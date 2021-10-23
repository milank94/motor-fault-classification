"""
Any config specific to model training step goes here.
"""

# General configuration
MONITOR = 'val_loss'
VAL_SPLIT = 0.2
LSTM_UNITS = 100
OPTIMIZER = 'adam'
EPOCHS = 100

# +
# Binary classification
# OUTPUT_SIZE = 1
# ACTIVATION = 'sigmoid'
# LOSS_FUNCTION = 'binary_crossentropy'
# -

# Multi-class classification
OUTPUT_SIZE = 3
ACTIVATION = 'softmax'
LOSS_FUNCTION = 'sparse_categorical_crossentropy'
