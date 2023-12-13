# -*- coding: utf-8 -*-
"""Copy of Repository.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZAky2RO4oLXWUPdNKnsEFfgpMhRszrkC
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Upload the required files
from google.colab import files
files.upload()

# Load the dataset from the file
data = pd.read_csv('online_shoppers_intention.csv')
data

#Checking for Missing Values
# Check if there are any missing values in each column
missing_values = data.isnull().sum()
missing_values

# Encoding Categorical Features
# One-hot encoding for categorical features
data_encoded = pd.get_dummies(data, columns=['Month', 'VisitorType', 'Weekend'])
data_encoded

# Data Normalization
# Selecting only numerical features for normalization
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
numerical_features

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Apply the scaler to the numerical features in the encoded dataset
data_encoded[numerical_features] = scaler.fit_transform(data_encoded[numerical_features])

# Splitting the Dataset
# Separating the features and the target variable ('Revenue')
X = data_encoded.drop('Revenue', axis=1)
y = data_encoded['Revenue']

# Splitting the dataset into a training set (70%) and a testing set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Displaying the first few rows of the normalized and split dataset
X_train.head(), y_train.head()

"""Initialising the package"""

# Creating the main package directory
!mkdir ShopSightPredictPro

# Creating subdirectories for the package
!mkdir ShopSightPredictPro/shop_sight_predict_pro
!mkdir ShopSightPredictPro/tests

import sys
sys.path.append('/content/ShopSightPredictPro')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/shop_sight_predict_pro/__init__.py

# Commented out IPython magic to ensure Python compatibility.
# %%writefile /content/ShopSightPredictPro/shop_sight_predict_pro/data_processing.py
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
# 
# class DataLoader:
#     @staticmethod
#     def load_data(file_path):
#         return pd.read_csv(file_path)
# 
# class DataPreprocessor:
#     def __init__(self, data):
#         self.data = data
# 
#     def clean_data(self):
#         # Handle missing values
#         self.data = self.data.dropna()
# 
#         # Remove duplicates
#         self.data = self.data.drop_duplicates()
# 
#         return self.data
# 
#     def preprocess_data(self):
#         # Encoding categorical variables
#         self.data = pd.get_dummies(self.data)
# 
#         # Feature scaling for numerical columns
#         scaler = MinMaxScaler()
#         numerical_columns = self.data.select_dtypes(include=['int64', 'float64']).columns
#         self.data[numerical_columns] = scaler.fit_transform(self.data[numerical_columns])
# 
#         return self.data
# 
# 
#

data

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/shop_sight_predict_pro/model_training.py
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# 
# class ModelTrainer:
#     def __init__(self, model=LogisticRegression()):
#         self.model = model
# 
#     def train(self, X_train, y_train):
#         self.model.fit(X_train, y_train)
#         return self.model
# 
#     def predict(self, X):
#         return self.model.predict(X)
# 
# class ModelEvaluator:
#     @staticmethod
#     def evaluate(y_true, y_pred):
#         accuracy = accuracy_score(y_true, y_pred)
#         precision = precision_score(y_true, y_pred)
#         recall = recall_score(y_true, y_pred)
#         f1 = f1_score(y_true, y_pred)
#         return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1_score": f1}
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/shop_sight_predict_pro/utils.py
# from sklearn.model_selection import train_test_split
# 
# def split_data(X, y, test_size=0.3, random_state=42):
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
#     return X_train, X_test, y_train, y_test
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/tests/__init__.py

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/tests/test_data_processing.py
# import unittest
# import pandas as pd
# from shop_sight_predict_pro.data_processing import DataLoader, DataPreprocessor
# 
# class TestDataProcessing(unittest.TestCase):
# 
#     @classmethod
#     def setUpClass(cls):
#         # Assuming the file is in the same directory as the notebook
#         cls.file_path = 'online_shoppers_intention.csv'
#         cls.raw_data = DataLoader.load_data(cls.file_path)
#         cls.preprocessor = DataPreprocessor(cls.raw_data)
# 
#     def test_load_data_not_empty(self):
#         self.assertFalse(self.raw_data.empty)
# 
#     def test_clean_data_no_nulls(self):
#         cleaned_data = self.preprocessor.clean_data()
#         self.assertFalse(cleaned_data.isnull().any().any())
# 
#     def test_clean_data_no_duplicates(self):
#         cleaned_data = self.preprocessor.clean_data()
#         self.assertEqual(len(cleaned_data), len(cleaned_data.drop_duplicates()))
# 
#     def test_preprocess_data_encoded(self):
#         processed_data = self.preprocessor.preprocess_data()
#         # Check if categorical columns are one-hot encoded, adjust column names as necessary
#         self.assertIn('Month_May', processed_data.columns)
# 
#     def test_preprocess_data_scaled(self):
#         processed_data = self.preprocessor.preprocess_data()
#         # Check if a known numerical column is scaled
#         # Replace 'NumericalColumn' with an actual column name from your dataset
#         self.assertTrue(processed_data['Administrative'].max() <= 1 and processed_data['Administrative'].min() >= 0)
# 
# if __name__ == '__main__':
#     unittest.main()
# 
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%writefile ShopSightPredictPro/tests/test_model_training.py
# import unittest
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from shop_sight_predict_pro.data_processing import DataLoader, DataPreprocessor
# from shop_sight_predict_pro.model_training import ModelTrainer, ModelEvaluator
# 
# class TestModelTraining(unittest.TestCase):
# 
#     @classmethod
#     def setUpClass(cls):
#         file_path = 'online_shoppers_intention.csv'
#         data = DataLoader.load_data(file_path)
#         preprocessor = DataPreprocessor(data)
#         processed_data = preprocessor.preprocess_data()
# 
#         X = processed_data.drop('Revenue', axis=1)  # Assuming 'Revenue' is the target
#         y = processed_data['Revenue']
# 
#         cls.X_train, cls.X_test, cls.y_train, cls.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#         cls.model_trainer = ModelTrainer()
#         cls.model_trainer.train(cls.X_train, cls.y_train)
# 
#     def test_train_model_not_none(self):
#         self.assertIsNotNone(self.model_trainer.model)
# 
#     def test_model_predictions(self):
#         predictions = self.model_trainer.predict(self.X_test)
#         self.assertEqual(len(predictions), len(self.y_test))
# 
#     def test_model_evaluation_metrics(self):
#         predictions = self.model_trainer.predict(self.X_test)
#         evaluation = ModelEvaluator.evaluate(self.y_test, predictions)
#         self.assertIn('accuracy', evaluation)
#         self.assertIn('precision', evaluation)
#         self.assertIn('recall', evaluation)
#         self.assertIn('f1_score', evaluation)
# 
# if __name__ == '__main__':
#     unittest.main()
#

!ls /content/ShopSightPredictPro/shop_sight_predict_pro

!cat /content/ShopSightPredictPro/shop_sight_predict_pro/data_processing.py

import sys
sys.path.append('/content/ShopSightPredictPro')

from shop_sight_predict_pro.data_processing import DataLoader, DataPreprocessor

!python -m pytest /content/ShopSightPredictPro/tests/test_data_processing.py
!python -m pytest /content/ShopSightPredictPro/tests/test_model_training.py