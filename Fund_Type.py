import pdfplumber

def get_fund_type(pdf_path):
    """
    Determine the type of fund based on the content of the first page of the PDF file.
    
    Parameters:
    pdf_path (str): The path to the PDF file.
    
    Returns:
    str: The type of fund ('FundA', 'FundB', or 'Unknown').
    """
    with pdfplumber.open(pdf_path) as pdf:
        first_page_text = pdf.pages[0].extract_text()
        if "ABC Growth Fund" in first_page_text:
            return 'FundA'
        elif "XYZ Value Fund" in first_page_text:
            return 'FundB'
        else:
            return 'Unknown'
