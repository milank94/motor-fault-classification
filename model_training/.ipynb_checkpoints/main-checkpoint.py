from pyprojroot import here as get_project_root
import os
os.chdir(get_project_root()) # hack for notebook development

# +
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import logging
import collections
import os
import re
from data_acquisition.main import get_data
from data_processing.main import get_train_test_data

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.preprocessing import sequence

from keras.models import load_model
from keras.callbacks import ModelCheckpoint

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)

logging.basicConfig(level=logging.INFO)
# -

dataset = get_data()

train_test_data = get_train_test_data(dataset)

# +
X_train = np.array(train_test_data.X_train)
X_test = np.array(train_test_data.X_test)

y_train = np.array(train_test_data.y_train)
y_test = np.array(train_test_data.y_test)
# -
X_train.shape

model = Sequential()
model.add(LSTM(100, input_shape=(X_train.shape[1], X_train.shape[2])))
#model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(3, activation='softmax'))


model.summary()

chk = ModelCheckpoint('best_model.pkl', monitor='val_loss', save_best_only=True, mode='auto', verbose=1)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(X_train, y_train, epochs=100, batch_size=int(X_train.shape[0]), callbacks=[chk], validation_split=0.2)

# +
#loading the model and checking accuracy on the test data
model = load_model('best_model.pkl')

from sklearn.metrics import accuracy_score
test_preds = model.predict_classes(X_test)
accuracy_score(y_test, test_preds)
# -

import matplotlib.pyplot as plt
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()


