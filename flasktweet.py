from flask import Flask, request, render_template
from indexer import *
from searcher import *

app = Flask(__name__)


init_flag = 0

@app.route('/')
def default():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    query = request.form['query']
    if not query:
        return render_template("resultNotFound.html")
        #return "error no query found"
    else:
        # global init_flag
        # test = init_flag
        # print "\n--------" + str(test) + "_______\n"
        # if not test:
        #     print "THIS IS THE FIRST POST REQUEST"
        #     #lucene.initVM()
        #     init_flag = 1

        results = search_abstract(query)
        # print results
        #results = search(searcher, analyzer, GLOBALDIRECTORY, query) #keepsearching till enter
        return render_template('resultFound.html', outputs=results)
