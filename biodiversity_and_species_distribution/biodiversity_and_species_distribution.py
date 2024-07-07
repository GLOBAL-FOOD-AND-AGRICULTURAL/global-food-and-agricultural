# biodiversity_and_species_distribution.py
import numpy as np
import matplotlib.pyplot as plt

def load_species_data(file_path):
    # Load species data from CSV file
    data = np.loadtxt(file_path, delimiter=",")
    return data

def calculate_biodiversity(data):
    # Calculate biodiversity metrics
    species_richness = len(np.unique(data[:, 0]))
    species_evenness = np.exp(-np.sum(np.square(data[:, 1])))

    return species_richness, species_evenness

def visualize_biodiversity(species_richness, species_evenness):
    # Visualize biodiversity metrics
    plt.bar(range(2), [species_richness, species_evenness])
    plt.xlabel("Biodiversity Metrics")
    plt.ylabel("Values")
    plt.title("Biodiversity Metrics")
    plt.show()

def calculate_species_distribution(data):
    # Calculate species distribution
    species_distribution = np.zeros(len(np.unique(data[:, 0])))
    for i in range(len(data)):
        species_distribution[data[i, 0] - 1] += data[i, 1]

    return species_distribution

def visualize_species_distribution(species_distribution):
    # Visualize species distribution
    plt.bar(range(len(species_distribution)), species_distribution)
    plt.xlabel("Species")
    plt.ylabel("Distribution")
    plt.title("Species Distribution")
    plt.show()

# Load species data
data = load_species_data("species_data.csv")

# Calculate biodiversity metrics
species_richness, species_evenness = calculate_biodiversity(data)

# Visualize biodiversity metrics
visualize_biodiversity(species_richness, species_evenness)

# Calculate species distribution
species_distribution = calculate_species_distribution(data)

# Visualize species distribution
visualize_species_distribution(species_distribution)
