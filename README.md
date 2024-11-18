# CleanPy Advanced

CleanPy Advanced is a Python package designed to assist with data preprocessing and anomaly detection tasks. This package includes various modules for cleaning, profiling, anomaly detection, pipeline construction, and validation. It is optimized to work with data analysis workflows, ensuring better data quality and enhanced performance of machine learning models.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
  - [Anomalies](#anomalies)
  - [Cleaning](#cleaning)
  - [Pipeline](#pipeline)
  - [Profiling](#profiling)
  - [Validation](#validation)
- [Testing](#testing)
- [Contributing](#contributing)
- [Documentation](#documentation)

## Features

- **Anomalies**: Detects and handles outliers in datasets using models like Isolation Forest and Local Outlier Factor (LOF).
- **Cleaning**: Provides functions for cleaning datasets by handling missing values, duplicates, and other preprocessing tasks.
- **Pipeline**: Allows you to create end-to-end pipelines that include preprocessing, model training, and evaluation steps.
- **Profiling**: Generates data profiling reports to help better understand the structure and content of datasets.
- **Validation**: Provides functionality for validating datasets, ensuring their integrity and consistency before analysis or modeling.

## Installation

To install the CleanPy Advanced package, follow these steps:

### Installation via `pip` (Recommended)

You can easily install CleanPy Advanced directly from the repository by running the following command:

```bash
pip install git+https://github.com/MilanLanghendries/expert-lab-sprint2-prototype.git
```

This will automatically install CleanPy Advanced along with its dependencies.

### Installation via `setup.py`

If you prefer to install the package from the source, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/MilanLanghendries/expert-lab-sprint2-prototype.git
cd expert-lab-sprint2-prototype
```

2. Install the required packages by running:

```bash
pip install .
```
This will install CleanPy Advanced and its dependencies as specified in the setup.py file.

### Optional: Create a virtual environment

To avoid conflicts with other Python packages, it's recommended to create a virtual environment:

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Active the virtual environment:

    * On Windows:

    ```bash
    venv\Scripts\activate
    ```

    * On macOS/Linux

    ```bash
    source venv/bin/activate
    ```

3. Install CleanPy Advanced in the virtual environment:

```bash
pip install .
```

## Usage

To use the modules within CleanPy Advanced, simply import them into your Python script:

```python
from cleanpy_advanced.anomalies import detect_outliers
from cleanpy_advanced.cleaning import clean_missing_values
from cleanpy_advanced.pipeline import create_pipeline
from cleanpy_advanced.profiling import generate_profile_report
from cleanpy_advanced.validation import validate_data
```

### Example Usage

#### Anomalies (Anomaly Detection)

```python
import pandas as pd
from cleanpy_advanced.anomalies import detect_outliers

# Sample DataFrame
df = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

# Detect outliers with contamination set to 0.1
result = detect_outliers(df, ["A", "B"], contamination=0.1)
print(result)
```

#### Cleaning (Handle Missing Values)

```python
from cleanpy_advanced.cleaning import clean_missing_values

# Clean missing values in a DataFrame
df = clean_missing_values(df, strategy='mean')
```

#### Pipeline (Create a Data Pipeline)

```python
from cleanpy_advanced.pipeline import create_pipeline

# Create and execute a simple data pipeline
pipeline = create_pipeline(steps=[
    ('clean', clean_missing_values),
    ('model', your_model)
])
pipeline.fit(X_train, y_train)
```

#### Profiling (Generate a Profile Report)

```python
from cleanpy_advanced.profiling import generate_profile_report

# Generate and save the profile report of a DataFrame
profile = generate_profile_report(df)
profile.to_file("data_profile.html")
```

#### Validation (Validate Dataset Integrity)

```python
from cleanpy_advanced.validation import validate_data

# Validate the data for missing values and duplicates
valid = validate_data(df)
```

## Modules

### Anomalies

This module focuses on detecting and handling anomalies (outliers) in the dataset using various methods like Isolation Forest and Local Outlier Factor (LOF). It is essential for identifying unusual data points that may distort your model's performance.

* detect_outliers(df, columns, contamination=0.1): Detects  outliers in the specified columns of a DataFrame.
    * df: The pandas DataFrame containing your data.
    * columns: The list of columns in which to detect outliers.
    * contamination: The proportion of outliers in the dataset. Default is 0.1.

### Cleaning

The cleaning module provides various functions to preprocess data, including handling missing values, duplicate rows, and more.

* clean_missing_values(df, strategy='mean'): Handles missing values in the dataset by filling them using a specified strategy (mean, median, or mode).
    * df: The pandas DataFrame.
    * strategy: The method used for imputation. Default is 'mean'.

### Pipeline

The pipeline module helps create and manage data processing pipelines. It simplifies the process of chaining multiple data transformation steps and models together.

* create_pipeline(steps): Constructs a data processing pipeline.
    * steps: A list of tuples where each tuple consists of a name and a transformer/estimator. The pipeline will apply these steps in sequence.

### Profiling

This module provides functionality to generate data profiling reports, helping to understand the structure and distribution of your data.

* generate_profile_report(df): Generates a profile report of a given DataFrame.
    * df: The pandas DataFrame to profile.

### Validation

The validation module ensures data integrity before proceeding with further processing. It checks for issues like missing values, duplicates, and out-of-bound values.

* validate_data(df): Validates the dataset for potential issues like missing values and duplicates.
    * df: The pandas DataFrame.

## Testing

This repository includes unit tests to ensure the functionality and correctness of each module. To run the tests, use the following command:

```bash
pytest
```

### Test Structure

Tests are located in the `tests/` directory, with individual test files for each module (e.g., `test_anomalies.py`, `test_cleaning.py`). The tests verify the core functionality, edge cases, and correctness of the methods.

## Contributing

We welcome contributions to CleanPy Advanced! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to your forked repository (git push origin feature-branch).
5. Open a pull request.

Please ensure your code adheres to the existing code style and includes tests where appropriate.

## Documentation

For more detailed documentation, refer to the following resources:

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/): Official documentation for Pandas, the core library for data manipulation and analysis in Python.
- [Scikit-learn Documentation](https://scikit-learn.org/stable/): Scikit-learn provides simple and efficient tools for data mining and data analysis, built on top of NumPy, SciPy, and matplotlib.
- [pytest Documentation](https://docs.pytest.org/en/stable/): Documentation for pytest, the testing framework used to ensure the correctness of the CleanPy Advanced package.
- [Isolation Forest Documentation (Scikit-learn)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html): Official documentation for the Isolation Forest model used for outlier detection in the `anomalies.py` module.
- [Local Outlier Factor Documentation (Scikit-learn)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html): Documentation for the Local Outlier Factor (LOF) algorithm used in outlier detection.
- [pandas-profiling Documentation](https://pandas-profiling.github.io/pandas-profiling/docs/): Official documentation for the `pandas-profiling` library, which is used for generating profiling reports in the `profiling.py` module.
