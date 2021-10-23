import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
import os
from data_acquisition.main import get_data
from data_processing.main import get_train_test_data
import model_training_config as config

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras.models import load_model
from keras.callbacks import ModelCheckpoint

from sklearn.metrics import accuracy_score

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

logging.basicConfig(level=logging.INFO)

# Model Development

# Load the data
dataset = get_data()

# Process the data and train/test split
train_test_data = get_train_test_data(dataset)


# Prepare the data
X_train = np.array(train_test_data.X_train)
X_test = np.array(train_test_data.X_test)

y_train = np.array(train_test_data.y_train)
y_test = np.array(train_test_data.y_test)

# Generating the model
model = Sequential()
model.add(LSTM(config.LSTM_UNITS, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(config.OUTPUT_SIZE, activation=config.ACTIVATION))
model.summary()


# Training the model
chk = ModelCheckpoint('best_model.pkl', monitor=config.MONITOR, save_best_only=True, mode='auto', verbose=1)
model.compile(loss=config.LOSS_FUNCTION, optimizer=config.OPTIMIZER, metrics=['accuracy'])
hist = model.fit(
    X_train,
    y_train,
    epochs=config.EPOCHS,
    batch_size=int(X_train.shape[0]),
    callbacks=[chk],
    validation_split=config.VAL_SPLOT
    )

# Model Validation
# Plotting training and validation accuracy per epoch
fig, axs = plt.subplots(nrows=1, figsize=(11, 9))
plt.rcParams['font.size'] = '14'

for label in (axs.get_xticklabels() + axs.get_yticklabels()):
    label.set_fontsize(14)

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])

axs.set_title('Model Accuracy')
axs.set_ylabel('Accuracy', fontsize=14)
axs.set_xlabel('Epoch', fontsize=14)
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# Loading the model and checking accuracy on the test data
model = load_model('best_model.pkl')

test_preds = model.predict_classes(X_test)
accuracy_score(y_test, test_preds)

# Comparing the actual values versus the predicted values
data_dict = {0: 'normal', 1: 'horizontal misalignment', 2: 'imbalance'}
results = pd.DataFrame([y_test, test_preds]).T
results.columns = ['Actual', 'Prediction']
results.applymap(lambda x: data_dict[x])
