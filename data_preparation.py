import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_trf')

def load_and_preprocess_data():
    # Load dataset
    df = pd.read_csv('large_dummy_legal_dataset.csv')

    # Process documents
    df['processed_text'] = df['text'].apply(lambda x: preprocess_document(x))

    return df

def preprocess_document(text):
    # Tokenization, NER, etc.
    doc = nlp(text)
    tokens = [token.text for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Combine tokens back into a processed text
    processed_text = " ".join(tokens)
    return processed_text

def save_preprocessed_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    df = load_and_preprocess_data()
    save_preprocessed_data(df, 'preprocessed_data.csv')
