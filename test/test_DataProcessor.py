import unittest
from DataProcessor import DataProcessor
from ModelProcessor import ModelProcessor
# Import other class files as needed

class TestDataProcessor(unittest.TestCase):
    def test_load_data(self):
        # Create a DataProcessor instance
        data_processor = DataProcessor(data_path="test_data.csv")

        # Test loading data
        data = data_processor.load_data()

        # Assert that data is not None and has the correct shape
        self.assertIsNotNone(data)
        self.assertEqual(data.shape, (100, 10))  # Adjust shape as needed

    def test_preprocess_data(self):
        # Create a DataProcessor instance
        data_processor = DataProcessor(data_path="test_data.csv")

        # Load data
        data = data_processor.load_data()

        # Test preprocessing
        preprocessed_data = data_processor.preprocess_data(data)

        # Assert that preprocessed_data is not None and has the correct shape
        self.assertIsNotNone(preprocessed_data)
        self.assertEqual(preprocessed_data.shape, (100, 20))  # Adjust shape as needed
