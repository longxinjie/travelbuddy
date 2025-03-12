import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')