

def test_analyse_data_mock():
    from unittest.mock import Mock
    from inflammation.compute_data import analyse_data
    import numpy as np
    """
    Test the analyse_data function with a mock data source.
    """
    # Create a mock data source
    mock_data_source = Mock()
    
    # Define the mock return value for load_inflammation_data
    mock_data_source.load_inflammation_data.return_value = [
        np.array([[1, 2, 3], [4, 5, 6]]),
        np.array([[7, 8, 9], [10, 11, 12]])
    ]
    
    # Call the function to test
    result = analyse_data(mock_data_source)
    
    # Check if the result is as expected
    expected_result = np.array([[4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    assert np.array_equal(result, expected_result), "The analysed data does not match the expected result."


def test_analyse_data():
    from pathlib import Path
    import numpy as np
    from inflammation.compute_data import CSVDataSource
    from inflammation.compute_data import analyse_data
    """Test the analyse_data function with a real data source.
    This test checks if the function returns a non-empty numpy array with finite, non-negative values.
    """
    
    path = Path.cwd() / "../data"
    data_source = CSVDataSource(path)
    result = analyse_data(data_source)

    assert result is not None, "The result of analyse_data should not be None."
    assert isinstance(result, np.ndarray), "The result of analyse_data should be a numpy array."
    assert result.shape[0] > 0, "The result of analyse_data should have more than 0 rows."
    assert result.shape[1] > 0, "The result of analyse_data should have more than 0 columns."
    assert np.all(np.isfinite(result)), "The result of analyse_data should contain only finite values."
    assert np.all(result >= 0), "The result of analyse_data should contain only non-negative values."


def test_compute_standard_deviation_by_day():
    from inflammation.compute_data import compute_standard_deviation_by_day
    import numpy as np

    # Create mock data
    data = [
        np.array([[1, 2, 3], [4, 5, 6]]),
        np.array([[7, 8, 9], [10, 11, 12]])
    ]

    # Call the function to test
    result = compute_standard_deviation_by_day(data)

    # Check if the result is as expected
    expected_result = np.array([3.0, 3.0, 3.0])
    assert np.array_equal(result, expected_result), "The standard deviation by day does not match the expected result."
    assert result.ndim == 1, "The result should be a 1D array."