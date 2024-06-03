def check_accuracy(data):
    """
    Check the accuracy of extracted data.

    Parameters:
    data (dict): A dictionary containing extracted data fields.

    Returns:
    bool: True if the data is accurate, False otherwise.
    """
    errors = []

    # Check for missing values
    if not data.get('fund_name'):
        errors.append("Missing fund name")
    if not data.get('date'):
        errors.append("Missing date")
    if not data.get('client_name'):
        errors.append("Missing client name")
    if not data.get('account_number'):
        errors.append("Missing account number")
    if not data.get('investment_amount'):
        errors.append("Missing investment amount")
    if not data.get('return_rate'):
        errors.append("Missing return rate")

    # Check that all values fall within plausible ranges
    if data.get('investment_amount') and not is_valid_investment_amount(data['investment_amount']):
        errors.append("Invalid investment amount")

    # Additional checks as needed...

    # Return True if no errors were found, indicating that the data is accurate
    return len(errors) == 0

def is_valid_investment_amount(amount):
    """
    Check if the investment amount is within a plausible range.

    Parameters:
    amount (str): The investment amount to check.

    Returns:
    bool: True if the investment amount is valid, False otherwise.
    """
    # Implement logic to check if the investment amount is within a plausible range
    # For example, you could check if the amount is a positive number
    return amount.isdigit() and int(amount) > 0
