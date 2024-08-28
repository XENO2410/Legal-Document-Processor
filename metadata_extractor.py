import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_metadata(text):
    doc = nlp(text)
    metadata = {
        'court': extract_court(doc),
        'legal_provisions': extract_legal_provisions(doc),
        'petitioner': extract_petitioner(doc),
        'respondent': extract_respondent(doc),
        'case_number': extract_case_number(doc),
        'date_of_judgment': extract_date_of_judgment(doc),
        'judge': extract_judge(doc),
    }
    return metadata

def extract_court(doc):
    for ent in doc.ents:
        if ent.label_ == 'ORG' and 'court' in ent.text.lower():
            return ent.text
    return 'Court not found'

def extract_legal_provisions(doc):
    legal_provisions = []
    for ent in doc.ents:
        if ent.label_ == 'LAW':
            legal_provisions.append(ent.text)
    return legal_provisions if legal_provisions else ['Legal provisions not found']

def extract_petitioner(doc):
    for sent in doc.sents:
        if 'petitioner' in sent.text.lower():
            for ent in sent.ents:
                if ent.label_ in ['PERSON', 'ORG']:
                    return ent.text
    return 'Petitioner not found'

def extract_respondent(doc):
    for sent in doc.sents:
        if 'respondent' in sent.text.lower():
            for ent in sent.ents:
                if ent.label_ in ['PERSON', 'ORG']:
                    return ent.text
    return 'Respondent not found'

def extract_case_number(doc):
    for ent in doc.ents:
        if ent.label_ == 'CASE_NUMBER':
            return ent.text
    return 'Case number not found'

def extract_date_of_judgment(doc):
    for ent in doc.ents:
        if ent.label_ == 'DATE':
            return ent.text
    return 'Date of judgment not found'

def extract_judge(doc):
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'JUDGE']:
            return ent.text
    return 'Judge not found'
