import pandas as pd

def validate_data(file_path):
    try:
        df = pd.read_csv(file_path)
        assert not df.isnull().values.any(), "Missing values found!"
        print("Validation passed: No missing values.")
    except Exception as e:
        print(f"Validation failed: {e}")
        raise

if __name__ == "__main__":
    validate_data("data/input.csv")
