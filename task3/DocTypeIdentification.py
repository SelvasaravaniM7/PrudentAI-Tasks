def identify_document_type(document_text, forms):
    max_matches = 0
    identified_form = None

    for form, keywords in forms.items():
        matches = sum(keyword in document_text for keyword in keywords)
        if matches > max_matches:
            max_matches = matches
            identified_form = form

    return identified_form if max_matches > 0 else None


forms = {
    "ID Card": ["ID Number", "Date of Birth"],
    "IRS Form": ["Internal Revenue Service", "Taxpayer ID"],
    "Passport": ["Passport Number", "Nationality"],
    "Bank Statement": ["Account Number", "Transaction History"],
}

print(identify_document_type(
    "This is to certify that the ID Number is 12345, and the Date of Birth is 1990-01-01.", forms))  
print(identify_document_type(
    "Your Internal Revenue Service document requires your Taxpayer ID for filing.", forms))  
print(identify_document_type(
    "This document contains transaction history of the Account Number 987654321.", forms))  
print(identify_document_type(
    "This document does not contain any recognizable keywords.", forms))  
