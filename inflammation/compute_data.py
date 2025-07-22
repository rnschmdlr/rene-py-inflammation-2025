"""Module containing mechanism for calculating standard deviation between datasets."""


import numpy as np

from inflammation import models, views



def analyse_data(data_source):
    """
    Calculates the standard deviation by day between datasets.

    Expects the data source to provide inflammation data as a list of 2D NumPy arrays.
    """
    data = data_source.load_inflammation_data()
    if not data:
        raise ValueError("No data provided for analysis.")

    daily_std_dev = compute_standard_deviation_by_day(data)

    return daily_std_dev


def compute_standard_deviation_by_day(data):
    """
    Compute the standard deviation of inflammation data by day.

    :param data: List of 2D NumPy arrays containing inflammation data.
    :return: A 1D NumPy array containing the standard deviation for each day.
    """
    
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))
    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation
    