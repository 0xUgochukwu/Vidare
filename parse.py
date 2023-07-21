import os
from flask import Blueprint, jsonify
import PyPDF2
from pptx import Presentation
from app import app
from models import PitchDeckInfo, UploadedDocument, get_PitchDecks
parse_bp = Blueprint("parse", __name__)

@parse_bp.route('/parse/<document_id>', methods=['GET'])
def parse_and_store_pitch_deck(document_id):
    """Endpoint to parse the uploaded pitch deck document and store the extracted information."""
    uploaded_doc = UploadedDocument.get_by_id(document_id)
    if not uploaded_doc:
        return jsonify({'error': 'Document not found'}), 404

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_doc.file_path)

    if uploaded_doc.file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_number in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_number)
                slide_title = f"Slide {page_number + 1}"
                slide_content = page.extractText()
                metadata = pdf_reader.getDocumentInfo().author
                pitch_deck_info = PitchDeckInfo(slide_title, slide_content, metadata, document_id)
                pitch_deck_info.save()

    elif uploaded_doc.file_path.endswith('.pptx'):
        prs = Presentation(file_path)
        for slide in prs.slides:
            slide_title = slide.shapes.title.text
            slide_content = '\n'.join([shape.text for shape in slide.shapes if hasattr(shape, "text")])
            metadata = prs.core_properties.author
            pitch_deck_info = PitchDeckInfo(slide_title, slide_content, metadata, document_id)
            pitch_deck_info.save()

    else:
        return jsonify({'error': 'Unsupported file format'}), 400

    return jsonify({'message': 'File parsed and information stored successfully'}), 200

@parse_bp.route('/pitch_decks', methods=['GET'])
def fetch_pitch_decks():
    """ Endpoint to fetch all parsed pitch decks """
    decks = get_PitchDecks()
    return jsonify(decks)


@parse_bp.route('/pitch_deck/<document_id>', methods=['GET'])
def get_pitch_deck(document_id):
    """Endpoint to retrieve a particular pitch deck's slide information."""
    pitch_deck_info = PitchDeckInfo.query.filter_by(uploaded_document_id=document_id).all()

    if not pitch_deck_info:
        return jsonify({'error': 'Pitch deck not found'}), 404

    pitch_deck_data = []
    for pitch_deck in pitch_deck_info:
        pitch_deck_data.append({
            'slide_title': pitch_deck.slide_title,
            'slide_content': pitch_deck.slide_content,
            'metadata': pitch_deck.metadata
        })

    return jsonify({'pitch_deck': pitch_deck_data}), 200
