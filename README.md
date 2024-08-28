# Legal Document Classifier and Information Extractor

This project is a legal document classifier and information extractor designed to help legal professionals automate the classification of legal documents and extract crucial metadata such as petitioner, respondent, court, legal provisions, and more. Built with Python, Flask, and spaCy, the system leverages Natural Language Processing (NLP) techniques to understand and process legal documents.

## Features

- **Document Classification**: Classifies legal documents into types such as Special Leave Petition, Writ Petition, Statutory Appeal, Form 28, etc.
- **Entity Extraction**: Extracts important entities such as names of petitioners, respondents, legal provisions, and courts.
- **Metadata Extraction**: Automatically pulls out metadata from documents, including document type, involved parties, court name, and relevant legal provisions.
- **Dynamic Document Processing**: Upload a `.txt` legal document and get processed tokens, named entities, and metadata in an easy-to-read format.
- **Downloadable Processed Data**: The processed data can be downloaded as a JSON file for further analysis.

## Installation

To get the application running locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Create and activate a Python virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the spaCy models required for processing:

    ```bash
    python -m spacy download en_core_web_sm
    python -m spacy download en_core_web_trf
    ```

## Usage

### Running the Flask App

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000`.

3. Upload a `.txt` legal document, and the application will classify the document, extract important entities, and display metadata.

### Document Classifier

The document classifier uses `TfidfVectorizer` and `LogisticRegression` to classify legal documents into predefined categories like "Special Leave Petition", "Writ Petition", etc. It can be run separately or integrated within the Flask app.

To train and test the document classifier, run:

```bash
python document_classifier.py
```

### Preprocessing Documents

Use the `data_preparation.py` script to preprocess legal documents. This script tokenizes the text, extracts named entities, and saves the processed data to a JSON file.

Run the script as follows:

```bash
python data_preparation.py
```

The processed documents will be saved to `processed_data/dataset.json`.

## Folder Structure

```
|-- app.py                   # Main Flask app
|-- document_classifier.py    # Document classifier script
|-- data_preparation.py       # Document preprocessing script
|-- requirements.txt          # Project dependencies
|-- templates/
|   |-- index.html            # Home page
|   |-- results.html          # Results page
|-- static/
|   |-- style.css             # Custom styles (if any)
|-- processed_data/           # Folder where processed files are saved
|   |-- dataset.json
```

## Technologies Used

- **Flask**: For building the web application.
- **spaCy**: For natural language processing and entity recognition.
- **scikit-learn**: For building the document classifier.
- **Jinja2**: For rendering HTML templates.
- **Joblib**: For saving and loading models.
- **TfidfVectorizer**: For vectorizing document text.
