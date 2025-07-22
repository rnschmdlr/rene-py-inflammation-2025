#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os

from inflammation.models import CSVDataSource, JSONDataSource
from inflammation.compute_data import analyse_data


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles

    if args.full_data_analysis or args.plot:
        _, extension = os.path.splitext(infiles[0])
        if extension == '.json':
            data_source = JSONDataSource(os.path.dirname(infiles[0]))
        elif extension == '.csv':
            data_source = CSVDataSource(os.path.dirname(infiles[0]))
        else:
            raise ValueError(f'Unsupported data file format: {extension}')

    if args.full_data_analysis:    
        print(analyse_data(data_source))
    
    if args.plot:
        from inflammation import views
        from inflammation import models

        # Load the data from the specified files
        inflammation_data = data_source.load_inflammation_data()

        # Prepare the view data
        view_data = {
            'average': models.daily_mean(inflammation_data),
            'max': models.daily_max(inflammation_data),
            'min': models.daily_min(inflammation_data)
        }

        # Visualize the data
        views.visualize(view_data)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        '--full-data-analysis',
        action='store_true',
        dest='full_data_analysis')
    
    parser.add_argument(
        '--plot'
        , action='store_true',
        dest='plot',)

    args = parser.parse_args()

    main(args)
