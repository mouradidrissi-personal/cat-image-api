"""
Flask API for displaying cat images
"""
from flask import Flask, jsonify, render_template
import requests
from typing import List, Dict

app = Flask(__name__)

# Using the Cat API (free tier)
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
CAT_API_KEY = "YOUR_API_KEY_HERE"  # Get free key from https://thecatapi.com

@app.route('/')
def index():
    """Main page - list of cat images"""
    return render_template('index.html')

@app.route('/api/cats', methods=['GET'])
def get_cats():
    """Get random cat images"""
    try:
        params = {
            'limit': 10,
            'api_key': CAT_API_KEY
        }
        response = requests.get(CAT_API_URL, params=params)
        response.raise_for_status()
        cats = response.json()
        return jsonify({
            'success': True,
            'data': cats,
            'count': len(cats)
        }), 200
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/cats/<int:count>', methods=['GET'])
def get_cats_with_count(count: int):
    """Get specific number of cat images"""
    if count < 1 or count > 25:
        return jsonify({
            'success': False,
            'error': 'Count must be between 1 and 25'
        }), 400
    
    try:
        params = {
            'limit': count,
            'api_key': CAT_API_KEY
        }
        response = requests.get(CAT_API_URL, params=params)
        response.raise_for_status()
        cats = response.json()
        return jsonify({
            'success': True,
            'data': cats,
            'count': len(cats)
        }), 200
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)