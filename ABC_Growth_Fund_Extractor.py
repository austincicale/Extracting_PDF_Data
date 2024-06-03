from extractors.base_extractor import PDFExtractor

class FundAExtractor(PDFExtractor):
    def extract_specific_data(self):
        """
        Extract specific data fields from an ABC Growth Fund PDF file.

        Returns:
        dict: A dictionary containing extracted data fields.
        """
        text = self.extract_text()
        lines = text.split('\n')
        data = {}
        for line in lines:
            if "Fund Name:" in line:
                data['fund_name'] = line.split(":")[1].strip()
            elif "Date:" in line:
                data['date'] = line.split(":")[1].strip()
            elif "Client Name:" in line:
                data['client_name'] = line.split(":")[1].strip()
            elif "Account Number:" in line:
                data['account_number'] = line.split(":")[1].strip()
            elif "Investment Amount:" in line:
                data['investment_amount'] = line.split(":")[1].strip()
            elif "Return Rate:" in line:
                data['return_rate'] = line.split(":")[1].strip()
        data = self.match_entity_id(data)
        return data
