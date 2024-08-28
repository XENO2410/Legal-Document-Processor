import random
import pandas as pd

# Sample names for petitioners and respondents
petitioner_names = ["Rajesh Kumar", "Priya Nair", "Amit Sharma", "Sunita Mehta", "Vikram Singh", "Anjali Verma"]
respondent_names = ["State of Kerala", "State of Uttar Pradesh", "State of Maharashtra", "State of Tamil Nadu", "State of Karnataka", "Government of India"]
courts = ["Supreme Court of India", "High Court of Kerala", "High Court of Bombay", "High Court of Delhi", "High Court of Karnataka"]
legal_provisions = [
    "Article 136 of the Constitution of India", 
    "Section 302 of the Indian Penal Code, 1860", 
    "Section 260A of the Income Tax Act, 1961", 
    "Article 226 of the Constitution of India", 
    "Land Acquisition Act, 2013"
]
document_types = ["Special Leave Petition", "Statutory Appeal", "Writ Petition", "Form 28"]

# Function to generate a single dummy document
def generate_dummy_document():
    petitioner = random.choice(petitioner_names)
    respondent = random.choice(respondent_names)
    court = random.choice(courts)
    provision = random.choice(legal_provisions)
    doc_type = random.choice(document_types)
    
    text = f"""
    Petitioner: {petitioner}
    Respondent: {respondent}
    
    Filed under {provision}.
    
    {petitioner}, a resident of {random.choice(['Mumbai', 'Delhi', 'Chennai', 'Bengaluru', 'Kolkata'])}, files this {doc_type} in the {court}. 
    The petitioner challenges the judgment passed by the {random.choice(['High Court', 'Tribunal'])} under {provision}.
    
    Address of Petitioner: {random.randint(1, 100)}, {random.choice(['MG Road', 'LBS Road', 'Link Road', 'Ring Road'])}, {random.choice(['Mumbai', 'Delhi', 'Chennai', 'Bengaluru', 'Kolkata'])}, India.
    Address of Respondent: Secretariat, {random.choice(['Thiruvananthapuram', 'Lucknow', 'Mumbai', 'Chennai', 'Bengaluru'])}, {random.choice(['Kerala', 'Uttar Pradesh', 'Maharashtra', 'Tamil Nadu', 'Karnataka'])}, India.
    """
    
    return text.strip(), doc_type

# Generate a large dataset
def generate_large_dummy_dataset(num_samples=10000):
    data = []
    for _ in range(num_samples):
        text, label = generate_dummy_document()
        data.append({"text": text, "label": label})
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_large_dummy_dataset()

# Save to CSV for later use
df.to_csv('large_dummy_legal_dataset.csv', index=False)
print("Dummy dataset created and saved as 'large_dummy_legal_dataset.csv'")
