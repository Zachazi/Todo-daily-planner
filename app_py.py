import os
from flask import Flask, render_template, send_from_directory

# Initialize the Flask application
app = Flask(__name__)

# Define the base directory for static files and templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Ensure the directories exist
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(os.path.join(STATIC_DIR, 'css'), exist_ok=True)
os.makedirs(os.path.join(STATIC_DIR, 'js'), exist_ok=True)

# Route for the home page
@app.route('/')
def index():
    """
    Renders the main index.html template.
    """
    return render_template('index.html')

# Route to serve static files (CSS, JS)
@app.route('/static/<path:filename>')
def static_files(filename):
    """
    Serves static files from the 'static' directory.
    This includes CSS and JavaScript files.
    """
    return send_from_directory(STATIC_DIR, filename)

# Run the Flask app
if __name__ == '__main__':
    # The debug mode allows for automatic reloading on code changes
    # and provides a debugger. Set to False in production.
    app.run(debug=True)