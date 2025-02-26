import re

def validate_input(data):
    def validate_ssn(ssn):
        return re.match(r"^\d{3}-\d{2}-\d{4}$", ssn) is not None

    def validate_email(email):
        return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is not None

    def validate_credit_card(card_number):
        return re.match(r"^\d{4}-?\d{4}-?\d{4}-?\d{4}$", card_number) is not None

    def validate_cvv(cvv):
        return re.match(r"^\d{3,4}$", cvv) is not None

    def validate_pan(pan):
        return re.match(r"^[A-Z]{5}\d{4}[A-Z]{1}$", pan) is not None

    def validate_isin(isin):
        return re.match(r"^[A-Z]{2}[A-Z0-9]{9}\d{1}$", isin) is not None

    def validate_vin(vin):
        return re.match(r"^[A-HJ-NPR-Z0-9]{17}$", vin) is not None

    def validate_drivers_id(drivers_id):
        return re.match(r"^[A-Z0-9]{1,20}$", drivers_id) is not None

    validated_data = {}
    if 'ssn' in data and validate_ssn(data['ssn']):
        validated_data['ssn'] = data['ssn']
    if 'email' in data and validate_email(data['email']):
        validated_data['email'] = data['email']
    if 'credit_card' in data and validate_credit_card(data['credit_card']):
        validated_data['credit_card'] = data['credit_card']
    if 'cvv' in data and validate_cvv(data['cvv']):
        validated_data['cvv'] = data['cvv']
    if 'pan' in data and validate_pan(data['pan']):
        validated_data['pan'] = data['pan']
    if 'isin' in data and validate_isin(data['isin']):
        validated_data['isin'] = data['isin']
    if 'vin' in data and validate_vin(data['vin']):
        validated_data['vin'] = data['vin']
    if 'drivers_id' in data and validate_drivers_id(data['drivers_id']):
        validated_data['drivers_id'] = data['drivers_id']
    
    return validated_data
