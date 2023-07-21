from flask import Flask
from models import db

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'pptx'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitchdeck.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register blueprints for different components
from upload import upload_bp
from parse import parse_bp

app.register_blueprint(upload_bp)
app.register_blueprint(parse_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

