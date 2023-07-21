import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UploadedDocument(db.Model):
    """Model for storing information about uploaded documents."""
    id = db.Column(db.String(36), primary_key=True)
    file_path = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)

    def __init__(self, file_path, title):
        self.id = str(uuid.uuid4())
        self.file_path = file_path
        self.title = title

    def save(self):
        """Save the document information to the database."""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, document_id):
        """Retrieve an uploaded document by its ID."""
        return cls.query.get(document_id)


def get_uploaded_documents():
    """Retrieve all uploaded documents."""
    return UploadedDocument.query.all()



class PitchDeckInfo(db.Model):
    """Model for storing extracted pitch deck information."""
    id = db.Column(db.String(36), primary_key=True)
    slide_title = db.Column(db.String(255))
    slide_content = db.Column(db.Text)
    deck_metadata = db.Column(db.Text)
    uploaded_document_id = db.Column(db.String(36), db.ForeignKey('uploaded_document.id'))

    def __init__(self, slide_title, slide_content, metadata, uploaded_document_id):
        self.id = str(uuid.uuid4())
        self.slide_title = slide_title
        self.slide_content = slide_content
        self.deck_metadata = metadata
        self.uploaded_document_id = uploaded_document_id

    def save(self):
        """Save the pitch deck information to the database."""
        db.session.add(self)
        db.session.commit()



def get_PitchDecks():
    """Retrieve all Pitch Deck Info."""
    return PitchDeckInfo.query.all()


