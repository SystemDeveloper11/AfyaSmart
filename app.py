import os
import json
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a-very-secret-key-that-you-should-change')

# Dummy user database for local storage
USERS_DB_FILE = 'data/users.json'

# Ensure the data directory exists
os.makedirs(os.path.dirname(USERS_DB_FILE), exist_ok=True)

def get_users_data():
    if not os.path.exists(USERS_DB_FILE):
        with open(USERS_DB_FILE, 'w') as f:
            json.dump([], f)
    with open(USERS_DB_FILE, 'r') as f:
        return json.load(f)

def save_users_data(data):
    with open(USERS_DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle user registration and save data locally
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        users = get_users_data()
        users.append({'name': name, 'email': email, 'phone': phone})
        save_users_data(users)
        
        # Set a session variable to indicate the user is registered
        session['registered'] = True
        
        # Redirect to the chat page after successful registration
        return redirect(url_for('chat'))
    
    return render_template('register.html')

@app.route('/chat')
def chat():
    # Check if the user is registered before allowing access
    if not session.get('registered'):
        return redirect(url_for('index'))
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def get_gemini_response():
    # Check if the user is registered
    if not session.get('registered'):
        return jsonify({'error': 'Unauthorized access.'}), 403

    user_message = request.json.get('message')

    # Comprehensive list of health-related keywords from check_health_related.php
    health_keywords = [
        'health', 'medical', 'medicine', 'treatment', 'diagnosis', 'symptom',
        'symptoms', 'disease', 'illness', 'pain', 'ache', 'fever', 'headache',
        'cough', 'flu', 'malaria', 'diabetes', 'doctor', 'hospital', 'pain'
    ]
    
    is_health_related = any(keyword in user_message.lower() for keyword in health_keywords)

    if is_health_related:
        return jsonify({'response': "I'm sorry, as AfyaSmart, I cannot give medical advice. Please consult a professional healthcare provider."})
    else:
        # Use the Gemini API to get a response
        # Retrieve the API key from the environment variable named GEMINI_API_KEY
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return jsonify({'error': 'API key not found.'}), 500

        # API endpoint URL
        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

        # Request payload
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": user_message}
                    ]
                }
            ],
            "tools": [{"google_search": {}}]
        }

        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status() # Raise an exception for bad status codes
            data = response.json()
            generated_text = data['candidates'][0]['content']['parts'][0]['text']
            return jsonify({'response': generated_text})
        except requests.exceptions.RequestException as e:
            print(f"Error calling Gemini API: {e}")
            return jsonify({'error': 'Failed to get a response from AfyaSmart.'}), 500

@app.route('/api/symptoms', methods=['POST'])
def check_symptoms():
    user_query = request.json.get('query', '').lower()
    
    try:
        # Load data from the provided JSON files
        with open('data/health_knowledge.json', 'r') as f:
            health_knowledge = json.load(f)
        
        with open('data/health_faq.json', 'r') as f:
            health_faq = json.load(f)

        # Search health knowledge for matching keywords
        for item in health_knowledge:
            if any(keyword.lower() in user_query for keyword in item['keywords']):
                return jsonify({'success': True, 'answer': item['response']})

        # Search FAQ for matching questions
        for item in health_faq:
            if item['question'].lower() in user_query:
                return jsonify({'success': True, 'answer': item['answer']})

    except (IOError, json.JSONDecodeError) as e:
        return jsonify({'success': False, 'answer': f'Error loading data files in AfyaSmart: {str(e)}'})

    return jsonify({'success': False, 'answer': 'No information found. Please try a different query.'})

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)
