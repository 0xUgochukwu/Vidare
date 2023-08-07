
<h1 align="center">Vidare<h1>
<h3 align="center">Pitch Deck Parser<h3>

> This repository contains a powerful and user-friendly Python-based backend solution for parsing uploaded pitch deck documents
>
> The application is designed to handle popular formats like PDF and PowerPoint, extracting essential information such as
> slide titles, content, and metadata.

### Features:

- API Endpoint for File Uploads: Our application provides a robust API endpoint that allows users to effortlessly upload pitch deck documents directly from their devices.

- Document Parsing Module: We have implemented a sophisticated module that efficiently parses uploaded pitch decks using pdfplumber, PyPDF2 and python-pptx libraries. This module extracts slide titles and content, ensuring accurate and reliable results.

- Database Integration: To ensure seamless retrieval and analysis of extracted information, we have implemented a well-structured database schema using Flask-SQLAlchemy. All parsed data is stored securely for future use.

- Error Handling and Validation: Our application includes comprehensive error handling and validation mechanisms to handle diverse file types, sizes, and any potential parsing issues gracefully.

### Getting Started:

To set up and run the application, open up your terminal and follow these simple steps:

Note: Make sure you have Python V3.6 or above installed on your system, to confirm run this command:
```bash
python --version
```

#### Installation
```bash
git clone https://github.com/0xUgochukwu/Vidare.git
cd Vidare
```

#### Setting up the Application
- Create a virtual environment
```bash
python -m venv venv
```

- Activate it
For Windows:
```bash
venv\Scripts\activate
```
For Mac/Linux users:
```bash
source venv/bin/activate
```

- Install the requirements in your virtual environment using pip:
```bash
pip install -r requirements.txt
```

- Run the Application:
```bash
python app.py
```
Copy the link provided by the system as the base url for the application (usually: `http://127.0.0.1:5000`)


#### Usage
Now you can test the application using postman or any other API testing tools:
If you don't know how to use postman then watch this video guide where I explain how to test this app with postman: [Video Guide](https://youtu.be/8HiVti4f59c)

If you know how to use postman then use these endpoints and parameters available in the application:

List of Endpoints
---
| Endpoint                                         | Requirements                                                | Functionality                                                     |
| ------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- |
| `http://127.0.0.1:5000/upload`                   | `<file>`, `<title>` to be passed as parameters to form data | Uploads a pitch deck                                              |
| `http://127.0.0.1:5000/uploaded_documents`       |                                                             | gets the uploaded documents id's which will be in other endpoints |
| `http://127.0.0.1:5000/parse/<document_id>`      | `<document_id>` to be passed as part of the url             |  parses an uploaded document                                      |
| `http://127.0.0.1:5000/pitch_deck/<document_id>` | `<document_id>` to be passed as part of the url             | gets the stored details of a parsed document                      |

### Environment
* Language: Python v3.6

### Author
- Ugochukwu Chukwuma

