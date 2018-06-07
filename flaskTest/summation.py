from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['query']
    if not text:
        return render_template("resultNotFound.html")
        #return "error no query found"
    else:
        num = int(text)
        outputs = []
        sum = 0
        for i in range(1, num):
            output = {}
            output['index'] = i
            output['result'] = sum
            sum += i
            outputs.append(output)
        return render_template('resultFound.html', outputs=outputs)


