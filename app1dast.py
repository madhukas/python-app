# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Intentional vulnerability: inadequate session management
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check credentials (vulnerable for simplicity)
    if username == 'admin' and password == 'password':
        session['username'] = username  # Store username in session
        return redirect(url_for('dashboard'))
    else:
        return 'Login failed!'

# Intentional vulnerability: insecure direct object reference (IDOR)
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

