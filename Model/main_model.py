import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import json
import os

def load_data(file_path):
    """Load the CSV file."""
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """Convert categorical data to numerical and perform any required preprocessing."""
    df['Day_of_Week'] = df['Day_of_Week'].astype('category').cat.codes
    df['Hour_of_Day'] = df['Hour_of_Day'].astype('category').cat.codes
    return df

def feature_engineering(df):
    """Extract features and target variable."""
    features = ['Hour_of_Day', 'Day_of_Week', 'Time_Since_Last_Collection', 'Collection_Interval']
    X = df[features]
    y = df['Time_Until_Next_Collection']
    return X, y

def train_model(X_train, y_train):
    """Train the Random Forest model."""
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return the RMSE."""
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    return rmse

def predict_collection_times(model, X):
    """Use the trained model to predict collection times."""
    return model.predict(X)

def generate_schedule(df, num_trucks=10):
    """Generate a collection schedule based on the predicted collection times."""
    df = df.sort_values(by='Predicted_Time_Until_Next_Collection')
    unique_bins = df.drop_duplicates(subset=['Bin_ID'], keep='first')  # Ensure no duplicate bin entries

    truck_assignments = {}
    for i, row in enumerate(unique_bins.itertuples()):
        truck_id = i % num_trucks
        if truck_id not in truck_assignments:
            truck_assignments[truck_id] = []
        truck_assignments[truck_id].append((row.Bin_ID, row.Predicted_Time_Until_Next_Collection))

    return truck_assignments

def save_schedule_to_json(truck_assignments, output_file):
    schedule = []
    for truck_id, assignments in truck_assignments.items():
        schedule.append(truck_id + 1)
        list_schedule = []
        for bin_id, time in assignments:
            list_schedule.append(bin_id)
        schedule.append(list_schedule)

    with open(output_file, 'w') as f:
        #if element in schedule is a list, those are the bins
        #if element in schedule is a int, that is the truck number
        #add a key named as the int, and put the list of bins as the value
        json.dump({schedule[i]: schedule[i + 1] for i in range(0, len(schedule), 2)}, f, indent=4)

def display_schedule(truck_assignments):
    """Display the generated schedule."""
    print(truck_assignments)
    schedule = []
    for truck_id, assignments in truck_assignments.items():
        bins_info = ', '.join([f"Bin {bin_id}" for bin_id, time in assignments])
        schedule.append(f"Truck {truck_id + 1}: {bins_info}")

    for line in schedule:
        print(line)

def run(file_path):
    """Main function to run the entire process."""
    df = load_data(file_path)
    df = preprocess_data(df)
    X, y = feature_engineering(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    rmse = evaluate_model(model, X_test, y_test)
    print(f'Root Mean Squared Error: {rmse}')

    df['Predicted_Time_Until_Next_Collection'] = predict_collection_times(model, X)
    truck_assignments = generate_schedule(df)

    # Construct output file path
    output_file = os.path.join('Model', 'JSONFiles', os.path.splitext(os.path.basename(file_path))[0] + '_schedule.json')

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    save_schedule_to_json(truck_assignments, output_file)
    print(f'Schedule saved to {output_file}')

    display_schedule(truck_assignments)

# Run the process for multiple files
for i in range(1, 11):
    run(f'./Model/DataFiles/bin_collection_data{i}.csv')
