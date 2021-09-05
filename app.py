from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome, are you ready to make your dream flight to the caribbean?!"

@app.route('/about')
def about():
    return 'This is the about page'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')