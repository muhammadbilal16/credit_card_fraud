# Importing Libraries

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Function To Automate Building
def train_model(csv_file):
    # Load data from CSV file into a pandas data frame
    df = pd.read_csv(csv_file)

    # Split the data into training and testing sets
    X = df.drop(['estimated_stock_pct'], axis=1)
    y = df['estimated_stock_pct']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a decision tree regressor on the training data
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model on the testing data
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    # Model Score
    model_score= model.score(X_train, y_train)

    # Print the performance metrics
    print("Mean Absolute Error: {:.2f}".format(mae))
    # Print model score
    print("Model score is: {:.2f}".format(model_score))