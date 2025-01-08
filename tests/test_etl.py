import os
import sys

# Add the root directory of the project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.etl_pipeline import process_data

def test_process_data():
    input_file = "data/input.csv"
    output_file = "data/summary.csv"
    process_data(input_file, output_file)
    assert os.path.exists(output_file), "Summary file not generated!"
