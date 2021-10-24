from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import load_model
from data_acquisition.main import get_save_data
from data_processing.main import get_save_train_test_data
import model_eval_config as config

# Load the data
dataset = get_save_data()

# Process the data and train/test split
train_test_data = get_save_train_test_data(dataset)

# Prepare the data
X_test = np.array(train_test_data.X_test)
y_test = np.array(train_test_data.y_test)

# Loading the model and checking accuracy on the test data
model_path = config.OUTPUT_DATA_DIR / Path('best_model.pkl')
model = load_model(model_path)
test_preds = np.argmax(model.predict(X_test), axis=-1)
print(accuracy_score(y_test, test_preds))

# Comparing the actual values versus the predicted values
data_dict = {
    0: 'normal',
    1: 'horizontal misalignment',
    2: 'imbalance',
    3: 'vertical misalignment',
    4: 'overhang',
    5: 'underhang'
    }
results = pd.DataFrame([y_test, test_preds]).T
results.columns = ['Actual', 'Prediction']
results.applymap(lambda x: data_dict[x])

print(results)
