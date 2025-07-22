"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import glob
import os
import json

class CSVDataSource:
    """
    Class to handle loading CSV data files.

    Expects a directory path containing CSV files matching a specific pattern,
    such as 'inflammation*.csv', for loading inflammation data.
    """

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        """Load inflammation data from CSV files in the specified directory."""
        csv_files = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        data = list(map(load_csv, csv_files))  # Load CSV files from the directory
        if not data:
            raise ValueError(f"No inflammation CSV files found in path {self.dir_path}")
        return data  # Return the list of 2D NumPy arrays with inflammation data

class JSONDataSource:
    """
    Class to handle loading JSON data files.

    Expects a directory path containing JSON files with inflammation data.
    """

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        """Load inflammation data from JSON files in the specified directory."""
        json_files = glob.glob(os.path.join(self.dir_path, '*.json'))
        if not json_files:
            raise ValueError(f"No JSON files found in path {self.dir_path}")

        for file in json_files:
            with open(file, 'r', encoding='utf-8') as f:
                content = json.load(f)
                return [np.array(entry['observations']) for entry in content]


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('inflammation values should be non-negative')
    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    return normalised
