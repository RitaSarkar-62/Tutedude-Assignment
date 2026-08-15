# Flask and MongoDB Web Application

## 1. Project Title

**Flask and MongoDB Web Application**

---

## 2. Project Description

This project is a web application developed using **Python Flask** and **MongoDB Atlas**.

The application allows users to submit their **name, email, and message** through a web form. The submitted information is validated by the Flask application and stored in a MongoDB Atlas database.

The project also provides an API endpoint that reads information from a local `data.json` file and returns the data in JSON format.

This project demonstrates the basic integration of a Flask web application with a cloud-based MongoDB database.

---

## 3. Project Objectives

The main objectives of this project are:

* To understand the fundamentals of Flask.
* To create a web application using Python.
* To create and handle Flask routes.
* To create an HTML form.
* To process form data using Flask.
* To connect Flask with MongoDB Atlas.
* To store submitted data in MongoDB.
* To create a simple JSON API.
* To understand GET and POST requests.
* To use environment variables for database configuration.
* To implement basic input validation and error handling.
* To manage project dependencies using `requirements.txt`.

---

## 4. Technologies Used

| Technology    | Version / Purpose                       |
| ------------- | --------------------------------------- |
| Python        | Programming language                    |
| Flask         | 3.1.3 — Web framework                   |
| PyMongo       | 4.17.0 — MongoDB connectivity           |
| MongoDB Atlas | Cloud database                          |
| python-dotenv | 1.2.2 — Environment variable management |
| HTML          | Frontend structure                      |
| JSON          | Data storage and API response           |
| Git           | Version control                         |
| GitHub        | Source code repository                  |

---

## 5. Project Structure

```text
Flask_and_MongoDB_Rita/
│
├── app.py
├── data.json
├── requirements.txt
├── index.html
├── success.html
├── README.md
├── .env
└── .gitignore
```

### File Description

### `app.py`

The main Python file of the application.

It contains:

* Flask application setup
* MongoDB Atlas connection
* Application routes
* Form processing
* Input validation
* MongoDB data insertion
* API functionality
* Error handling

### `index.html`

The main webpage of the application.

It contains the form through which users provide their:

* Name
* Email
* Message

### `success.html`

This page is displayed after the form has been successfully submitted and the data has been stored in MongoDB.

### `data.json`

A JSON file containing data that is read by the `/api` endpoint.

### `requirements.txt`

Contains the Python packages and their versions required to run the project.

### `README.md`

Contains the complete documentation of the project.

### `.env`

Contains environment variables such as the MongoDB connection URI.

**The actual `.env` file should not be uploaded to GitHub if it contains private credentials.**

### `.gitignore`

Specifies files and folders that should not be uploaded to GitHub.

---

# 6. Python Dependencies

The project uses the following packages:

```text
blinker==1.9.0
click==8.4.2
colorama==0.4.6
dnspython==2.8.0
Flask==3.1.3
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
pymongo==4.17.0
python-dotenv==1.2.2
Werkzeug==3.1.8
```

These dependencies are stored in `requirements.txt`.

They can be installed using:

```bash
pip install -r requirements.txt
```

---

# 7. Flask Application

Flask is a lightweight Python web framework used to develop the application.

The Flask application is initialized using:

```python
app = Flask(__name__)
```

Flask handles:

* HTTP requests
* Application routes
* HTML templates
* Form submissions
* Responses
* Error handling

---

# 8. MongoDB Atlas Integration

The project uses **MongoDB Atlas** as its database.

The MongoDB connection URI is stored in an environment variable called `MONGO_URI`.

The application loads the environment variables using:

```python
load_dotenv()
```

The MongoDB URI is then obtained using:

```python
MONGO_URI = os.getenv("MONGO_URI")
```

The application creates a MongoDB client using PyMongo:

```python
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)
```

The connection is tested using:

```python
client.admin.command("ping")
```

If the connection is successful, the application displays:

```text
MongoDB Atlas connected successfully!
```

---

# 9. MongoDB Database Structure

The application uses the following database structure:

```text
MongoDB Atlas
│
└── flask_mongodb_db
    │
    └── submissions
        │
        ├── name
        ├── email
        └── message
```

### Database

```text
flask_mongodb_db
```

### Collection

```text
submissions
```

Each submitted form is stored as a MongoDB document.

Example:

```json
{
    "name": "Rita",
    "email": "example@gmail.com",
    "message": "Hello"
}
```

---

# 10. Application Routes

The application contains the following routes:

| Route      | HTTP Method | Description                    |
| ---------- | ----------- | ------------------------------ |
| `/`        | GET         | Displays the main webpage      |
| `/api`     | GET         | Returns `data.json` as JSON    |
| `/submit`  | POST        | Processes and stores form data |
| `/success` | GET         | Displays the success page      |

---

# 11. Home Route

### URL

```text
/
```

### Method

```text
GET
```

The home route displays the main HTML page.

```python
@app.route("/")
def home():
    return render_template("index.html")
```

When a user visits the home page, Flask renders `index.html`.

---

# 12. API Route

### URL

```text
/api
```

### Method

```text
GET
```

The `/api` route reads data from the `data.json` file.

The file is opened using:

```python
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

The data is then returned using:

```python
return jsonify(data)
```

Therefore, when a user visits:

```text
http://127.0.0.1:5000/api
```

the contents of `data.json` are returned as a JSON response.

If an error occurs while reading the file, the application returns an error message with HTTP status code `500`.

---

# 13. Submit Route

### URL

```text
/submit
```

### Method

```text
POST
```

The `/submit` route handles the form submission.

The application receives the submitted values using:

```python
name = request.form.get("name")
email = request.form.get("email")
message = request.form.get("message")
```

The application checks whether all required fields have been entered.

```python
if not name or not email or not message:
```

If any field is empty, the user receives:

```text
All fields are required.
```

---

# 14. Storing Data in MongoDB

After successful validation, the application creates a document:

```python
document = {
    "name": name,
    "email": email,
    "message": message
}
```

The document is then inserted into the MongoDB collection using:

```python
collection.insert_one(document)
```

After successful insertion, the application redirects the user to the success page.

---

# 15. Success Route

### URL

```text
/success
```

### Method

```text
GET
```

The success route renders `success.html`.

```python
@app.route("/success")
def success():
    return render_template("success.html")
```

This page is displayed after the user's information has been successfully stored in MongoDB.

---

# 16. Input Validation

The application checks whether the user has entered all required information.

The required fields are:

* Name
* Email
* Message

If any field is missing, the form is not submitted to MongoDB.

Instead, the application displays:

```text
All fields are required.
```

This prevents incomplete submissions from being stored in the database.

---

# 17. Error Handling

The project includes basic error handling.

### MongoDB Connection Error

If the MongoDB connection fails, the application prints the connection error.

### MongoDB Unavailable

If MongoDB is not available when a user submits the form, the application displays:

```text
MongoDB connection is not available.
```

### Database Insertion Error

If an error occurs while inserting the document into MongoDB, the application displays the error message.

### API Error

If the application cannot read `data.json`, the `/api` endpoint returns an error response with HTTP status code `500`.

---

# 18. Environment Variables

The MongoDB connection string is stored in an environment variable rather than directly in the Python source code.

The `.env` file contains:

```text
MONGO_URI=your_mongodb_connection_string
```

The application loads this value using:

```python
load_dotenv()
```

and:

```python
os.getenv("MONGO_URI")
```

### Security

The `.env` file may contain sensitive MongoDB credentials.

Therefore, it should not be uploaded to GitHub.

The `.gitignore` file should contain:

```text
.env
.venv/
__pycache__/
```

---

# 19. Installation Requirements

Before running the project, install:

* Python
* MongoDB Atlas account
* Visual Studio Code
* Git (optional)

Python version can be checked using:

```bash
python --version
```

---

# 20. Installation Steps

## Step 1: Clone the Repository

Clone the project from GitHub:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Flask_and_MongoDB_Rita
```

---

## Step 2: Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows, activate it using:

```bash
.venv\Scripts\activate
```

---

## Step 3: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure MongoDB

Configure MongoDB Atlas and obtain the MongoDB connection URI.

Create a `.env` file in the project directory:

```text
MONGO_URI=your_mongodb_connection_string
```

Replace the value with your actual MongoDB Atlas connection string.

The application automatically loads the URI from the `.env` file.

---

# 21. Running the Application

After completing the setup, run:

```bash
python app.py
```

The Flask development server will start.

Open the URL displayed in the terminal.

Normally, the application will be available at:

```text
http://127.0.0.1:5000/
```

---

# 22. Application Workflow

The main application workflow is:

```text
User
  ↓
Open Website
  ↓
index.html
  ↓
Enter Name, Email and Message
  ↓
Submit Form
  ↓
/submit
  ↓
Validate Data
  ↓
MongoDB Atlas
  ↓
Insert Document
  ↓
/success
  ↓
success.html
```

### API Workflow

```text
User
  ↓
/api
  ↓
Read data.json
  ↓
Load JSON Data
  ↓
jsonify()
  ↓
JSON Response
```

---

# 23. Testing

The application can be tested using the following test cases.

### Test Case 1: Home Page

Open:

```text
http://127.0.0.1:5000/
```

**Expected Result:**

The main webpage should be displayed.

---

### Test Case 2: Valid Form Submission

Enter:

* Name
* Email
* Message

Then submit the form.

**Expected Result:**

The data should be stored in MongoDB and the user should be redirected to the success page.

---

### Test Case 3: Empty Form Field

Leave one or more fields empty and submit the form.

**Expected Result:**

The application should display:

```text
All fields are required.
```

---

### Test Case 4: API

Open:

```text
http://127.0.0.1:5000/api
```

**Expected Result:**

The contents of `data.json` should be returned as JSON.

---

### Test Case 5: MongoDB Verification

Open MongoDB Atlas and navigate to:

```text
flask_mongodb_db
    ↓
submissions
```

**Expected Result:**

The submitted information should appear as a document.

---

# 24. Git and GitHub

Git is used for version control and GitHub is used to store the project repository online.

Basic Git commands:

```bash
git add .
git commit -m "Add Flask MongoDB project"
git push
```

The GitHub repository should contain:

```text
app.py
data.json
requirements.txt
index.html
success.html
README.md
.gitignore
```

The `.env` file should be excluded from the repository if it contains the MongoDB credentials.

---

# 25. Advantages of the Project

This project provides practical experience with:

* Python programming
* Flask web development
* HTML forms
* Flask routing
* HTTP GET and POST requests
* MongoDB Atlas
* PyMongo
* JSON
* API development
* Environment variables
* Error handling
* Git
* GitHub

---

# 26. Future Improvements

The project can be further improved by adding:

* Email format validation
* Improved user interface
* User authentication
* Admin dashboard
* Display of stored submissions
* Update functionality
* Delete functionality
* Search functionality
* Pagination
* Advanced API functionality
* Better security
* Cloud deployment

---

# 27. Conclusion

This project demonstrates the integration of **Flask with MongoDB Atlas** to create a functional web application.

Users can submit their name, email, and message through an HTML form. Flask validates the submitted information and stores it in the MongoDB `submissions` collection.

The project also provides an API endpoint that reads information from `data.json` and returns it in JSON format.

Through this project, practical knowledge of **Python, Flask, MongoDB Atlas, PyMongo, HTML, JSON, environment variables, API development, and GitHub** is gained.

---

# 28. Author

**Name:** Rita Sarkar

**Project:** Flask and MongoDB Web Application


