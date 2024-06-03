from .base_extractor import PDFExtractor

class FundBExtractor(PDFExtractor):
    def extract_specific_data(self):
        text = self.extract_text()
        lines = text.split('\n')
        data = {}
        for line in lines:
            if "Report for" in line:
                data['fund_name'] = line.replace("Report for ", "").strip()
            elif "Report Date:" in line:
                data['date'] = line.split(":")[1].strip()
            elif "Name:" in line:
                data['client_name'] = line.split(":")[1].strip()
            elif "ID:" in line:
                data['account_number'] = line.split(":")[1].strip()
            elif "Initial Investment:" in line:
                data['investment_amount'] = line.split(":")[1].strip()
            elif "Current Value:" in line:
                data['current_value'] = line.split(":")[1].strip()
            elif "Performance:" in line:
                data['performance'] = line.split(":")[1].strip()
        data = self.match_entity_id(data)
        return data
