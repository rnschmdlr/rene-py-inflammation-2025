![Continuous Integration build in GitHub Actions](https://github.com/rnschmdlr/rene-py-inflammation-2025/actions/workflows/main.yml/badge.svg?branch=main)

# Introduction

This is a template software project repository used by the [Intermediate Research Software Development Skills In Python](https://github.com/carpentries-incubator/python-intermediate-development).


# Project Overview

This project analyzes inflammation data collected from patients over a series of days. It provides Python modules for loading, processing, and visualizing time-series medical data, with a focus on reproducible research workflows. The repository includes example datasets and analysis scripts to help users explore trends, compute statistics, and generate plots for inflammation studies.

# Features

- Modular Python code structure
- Automated testing with `pytest`
- Example data and scripts for analysis
- Continuous integration setup
- Ready-to-use documentation templates

# Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/carpentries-incubator/python-intermediate-development.git
    cd python-intermediate-development
    ```
2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

# Usage

- Run the main analysis script with one or more input CSV files as positional arguments:
    ```bash
    python src/inflammation_analysis.py data/inflammation-01.csv data/inflammation-02.csv
    ```
    - Each argument is the path to an input CSV file containing inflammation data for patients (required; one or more files can be specified).
    ```

# Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on submitting issues and pull requests.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Contact

For questions or support, please open an issue on the repository or contact the maintainers via GitHub.

# Acknowledgements

This template is developed as part of the Carpentries Incubator and is inspired by community best practices in research software engineering.
