import os

def scan_directory(directory_path):
    """
    Scan the directory for PDF files.
    
    Parameters:
    directory_path (str): The path to the directory containing PDF files.
    
    Returns:
    list: A list of PDF file paths.
    """
    pdf_files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.pdf')]
    return pdf_files
