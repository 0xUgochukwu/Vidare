from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create and configure the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'pptx'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitchdeck.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints for different components
from upload import upload_bp
from parse import parse_bp

app.register_blueprint(upload_bp)
app.register_blueprint(parse_and_store_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

