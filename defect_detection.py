def detect_defects(metadata):
    defects = []

    # Check if the court is found
    if metadata.get('court') == 'Court not found':
        defects.append('Court name is missing.')

    # Check if legal provisions are found
    if metadata.get('legal_provisions') == ['Legal provisions not found']:
        defects.append('Legal provisions are missing.')

    # Check if petitioner name is found
    if metadata.get('petitioner') == 'Petitioner not found':
        defects.append('Petitioner name is missing.')

    # Check if respondent name is found
    if metadata.get('respondent') == 'Respondent not found':
        defects.append('Respondent name is missing.')

    # Additional defect checks
    if metadata.get('case_number') == 'Case number not found':
        defects.append('Case number is missing.')

    if metadata.get('date_of_judgment') == 'Date of judgment not found':
        defects.append('Date of judgment is missing.')

    if metadata.get('judge') == 'Judge not found':
        defects.append('Judge name is missing.')

    if metadata.get('document_type') == 'Document type not classified':
        defects.append('Document type classification is missing.')

    return defects if defects else ['No defects detected.']
