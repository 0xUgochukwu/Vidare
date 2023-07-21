import os
import datetime
from flask import Blueprint, request, jsonify, current_app as app
from werkzeug.utils import secure_filename
from models import UploadedDocument, get_uploaded_documents


upload_bp = Blueprint("upload", __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@upload_bp.route('/upload', methods=['POST'])
def upload_pitch_deck():
    """Endpoint to handle file uploads and store information about the uploaded document."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        filename_with_timestamp = f"{timestamp}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_with_timestamp))

        # Save information about the uploaded document in the database
        uploaded_doc = UploadedDocument(file_path=filename_with_timestamp, title=filename)
        uploaded_doc.save()

        return jsonify({'message': 'File uploaded successfully', 'document_id': uploaded_doc.id}), 200

    return jsonify({'error': 'Invalid file format'}), 400

@upload_bp.route('/uploaded_documents', methods=['GET'])
def fetch_uploaded_documents():
    """Endpoint to fetch uploaded document IDs and titles."""
    uploaded_docs = get_uploaded_documents()
    documents_data = {doc.id: doc.title for doc in uploaded_docs}
    return jsonify(documents_data), 200

