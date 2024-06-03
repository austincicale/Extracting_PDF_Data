import pandas as pd

def save_to_csv(data, output_path):
    """
    Save extracted data to a CSV file.

    Parameters:
    data (dict): A dictionary containing extracted data fields.
    output_path (str): The path to save the CSV file.
    """
    df = pd.DataFrame([data])
    df.to_csv(output_path, index=False)
