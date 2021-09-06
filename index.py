from flask import Flask , render_template , request
import os

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/getFeedback' , methods = ['GET' , 'POST'])
def get_feedback():
    if request.method == 'POST':
        text = request.form['feedback']
        with open('read.txt', 'w') as f:
            f.write(str(text))
        os.system('python main_nltk.py')
        return "recieved"
        
    else:
        return render_template('get_feedback.html')

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
   app.run(debug = True)