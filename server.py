from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_result():
    name=request.form['name']
    location=request.form['location']
    language = request.form['language']
    comment= request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

if __name__== "__main__":
    app.run(debug=True)