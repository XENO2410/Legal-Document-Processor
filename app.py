from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
import spacy
import json
import csv
from document_classifier import classify_document
from metadata_extractor import extract_metadata
from defect_detection import detect_defects
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'processed_data'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max size for uploads

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            # Process the document
            processed_data = process_document(file_path)

            # Save processed data to JSON
            processed_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename + '_processed.json')
            with open(processed_file_path, 'w') as f:
                json.dump(processed_data, f, indent=4)

            # Redirect to results page
            return redirect(url_for('results', filename=filename + '_processed.json'))

        except Exception as e:
            flash(f"Error processing document: {str(e)}")
            return redirect(url_for('index'))
    
    flash('Invalid file format. Please upload a .txt file.')
    return redirect(url_for('index'))

@app.route('/results/<filename>')
def results(filename):
    # Load processed data from the JSON file
    try:
        processed_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(processed_file_path, 'r') as f:
            processed_data = json.load(f)
        
        tokens = processed_data['tokens']
        entities = processed_data['entities']
        metadata = processed_data['metadata']
        defects = processed_data.get('defects', 'No defects detected')

        return render_template('results.html', tokens=tokens, entities=entities, metadata=metadata, defects=defects, filename=filename)
    
    except FileNotFoundError:
        flash('Processed file not found.')
        return redirect(url_for('index'))

@app.route('/download/csv/<filename>')
def download_csv(filename):
    # Load processed data from the JSON file
    try:
        processed_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(processed_file_path, 'r') as f:
            processed_data = json.load(f)
        
        # Create a CSV file from the JSON data
        csv_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename.replace('.json', '.csv'))
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Token'])
            for token in processed_data['tokens']:
                writer.writerow([token])
            
            writer.writerow([])
            writer.writerow(['Entity', 'Label'])
            for entity, label in processed_data['entities']:
                writer.writerow([entity, label])
            
            writer.writerow([])
            writer.writerow(['Metadata', 'Value'])
            for key, value in processed_data['metadata'].items():
                writer.writerow([key, value])
            
            writer.writerow([])
            writer.writerow(['Defects'])
            writer.writerow([processed_data.get('defects', 'No defects detected')])
        
        return send_file(csv_file_path, as_attachment=True)

    except FileNotFoundError:
        flash('Processed file not found.')
        return redirect(url_for('index'))

def process_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        document_text = f.read()
    
    doc = nlp(document_text)
    tokens = [token.text for token in doc]
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Extract metadata using the document classifier and spaCy
    metadata = extract_metadata(document_text)

    # Detect defects in metadata
    defects = detect_defects(metadata)

    return {'tokens': tokens, 'entities': entities, 'metadata': metadata, 'defects': defects}

if __name__ == '__main__':
    app.run(debug=True)
