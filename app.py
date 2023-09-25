from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, static_url_path='/static')

def check_username(username):
    url = f"https://osu.ppy.sh/users/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    error_message_element = soup.find('h1', text='User not found! ;_;')
    
    if error_message_element:
        return "Username available"
    else:
        return "Username not available"

@app.route('/')
def username_checker():
    return render_template('username_checker.html')

@app.route('/usercheck')
def usercheck():
    return render_template('usercheck.html')

@app.route('/masscheck')
def masscheck():
    return render_template('masscheck.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/check_username', methods=['POST'])
def check_username_api():
    username = request.form.get('username')
    status = check_username(username)
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)