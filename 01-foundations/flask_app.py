"""
Flask Web Interface for AI Learning Journey
Week 2: Basic Flask Setup
"""

from flask import Flask, render_template, request, jsonify
import datetime
import sys
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Home page with AI learning dashboard"""
    return render_template('index.html')

@app.route('/api/info')
def get_info():
    """API endpoint to get system information"""
    info = {
        'message': 'AI Learning Journey Dashboard',
        'date': str(datetime.date.today()),
        'python_version': sys.version,
        'status': 'Flask is running successfully! 🎉'
    }
    return jsonify(info)

@app.route('/api/test', methods=['POST'])
def test_ai():
    """API endpoint for testing AI responses (placeholder for now)"""
    user_input = request.json.get('message', '')
    
    # Simple response logic (we'll improve this in later weeks)
    if 'hello' in user_input.lower():
        response = "Hello! Welcome to your AI learning journey! 🤖"
    elif 'how are you' in user_input.lower():
        response = "I'm doing great! Ready to help you learn AI! 🚀"
    elif 'weather' in user_input.lower():
        response = "I can help with weather data! We'll build that feature in Week 2. 🌤️"
    else:
        response = f"You said: '{user_input}'. I'm still learning! We'll add more intelligence soon. 🧠"
    
    return jsonify({
        'response': response,
        'timestamp': str(datetime.datetime.now()),
        'status': 'success'
    })

if __name__ == '__main__':
    print("🚀 Starting AI Learning Journey Web Interface...")
    print("📝 Open your browser to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
