from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import logging
from data_acquisition.main import get_save_data
from data_processing.main import get_save_train_test_data
import model_training_config as config

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint

logging.basicConfig(level=logging.INFO)

config.OUTPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Model Development
# Load the data
dataset = get_save_data()

# Process the data and train/test split
train_test_data = get_save_train_test_data(dataset)

# Prepare the data
X_train = np.array(train_test_data.X_train)
X_test = np.array(train_test_data.X_test)

y_train = np.array(train_test_data.y_train)
y_test = np.array(train_test_data.y_test)

# Generating the model
model = Sequential()
model.add(LSTM(config.LSTM_UNITS, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(config.OUTPUT_SIZE, activation=config.ACTIVATION))
print(model.summary())

# Training the model
model_path = config.OUTPUT_DATA_DIR / Path('best_model.pkl')
chk = ModelCheckpoint(model_path, monitor=config.MONITOR, save_best_only=True, mode='auto', verbose=1)
model.compile(loss=config.LOSS_FUNCTION, optimizer=config.OPTIMIZER, metrics=['accuracy'])
hist = model.fit(
    X_train,
    y_train,
    epochs=config.EPOCHS,
    batch_size=int(X_train.shape[0]),
    callbacks=[chk],
    validation_split=config.VAL_SPLIT
    )

# Model Validation
# Plotting training and validation accuracy per epoch
_, axs = plt.subplots(nrows=1, figsize=(11, 9))
file_location = config.OUTPUT_DATA_DIR / Path('plots/model_accuracy.png')
plt.rcParams['font.size'] = '14'

for label in (axs.get_xticklabels() + axs.get_yticklabels()):
    label.set_fontsize(14)

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])

axs.set_title('Model Accuracy')
axs.set_ylabel('Accuracy', fontsize=14)
axs.set_xlabel('Epoch', fontsize=14)
plt.legend(['train', 'val'], loc='upper left')
plt.savefig(file_location)
