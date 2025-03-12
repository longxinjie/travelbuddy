import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

@app.route('/')
def home():
    return render_template('index.html')