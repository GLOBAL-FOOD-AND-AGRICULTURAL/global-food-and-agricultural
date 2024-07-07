# energy_system_data_access.py
import pandas as pd

def load_energy_data(file_path):
    # Load energy data from CSV file
    data = pd.read_csv(file_path)
    return data

def process_energy_data(data):
    # Process energy data
    processed_data = data.dropna()  # Remove rows with missing values
    return processed_data

def visualize_energy_data(processed_data):
    # Visualize energy data
    import matplotlib.pyplot as plt
    plt.plot(processed_data['date'], processed_data['energy_consumption'])
    plt.xlabel('Date')
    plt.ylabel('Energy Consumption')
    plt.title('Energy Consumption Over Time')
    plt.show()
