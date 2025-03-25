from flask import Flask

app = Flask('Mlops-flask-app')

@app.route('/')
def home():
    return 'Welcome to MLOps with Flask'

app.run()