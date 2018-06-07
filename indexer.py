import sys, lucene, json
from os import path, listdir

#othershit dependencies
from org.apache.lucene.document import Document, Field, StringField, TextField
from org.apache.lucene.util import Version
from org.apache.lucene.store import RAMDirectory
from datetime import datetime

#Index dependencies
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
# from org.apache.lucene.store import SimpleFSDirectory

#retrieval dependencies
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, MultiFieldQueryParser, QueryParserBase


# ---------------------------- global constants ----------------------------- #
baseDirectory = path.dirname(path.abspath(sys.argv[0]))
textfileDirectory = baseDirectory + "/input/"
indexDirectory = baseDirectory + "/lucene_index/"
tokenCount = 128479 # Number of Tokens
fields = ["tweet", "u_name"]
loopVar = True
# print "Searcher Started"
GLOBALDIRECTORY = None

#INDEXING

#Returns array of .txt files to create documents
def getTxtFile(path):
    files = []
    for file in listdir(path): #lisdir(path) = all files in path that is passed in
        if file.endswith (".txt"): #makes sure no bullshit gets in
            files.append(file)
    return files

#Returns array of json objects
def getData(filename):
    path = textfileDirectory + filename
    dataArray = []
    with open(path) as file:

        for line in file:
            parsed_json = json.loads(line) #Each object is loaded in line by line
            dataArray.append(parsed_json)
    file.close()
    return dataArray


#creates document based off of jsonObject
def createDocument_tweet(data):
    jsonText = data['text'] #accesses tweet
    jsonName = data['user']['screen_name'] #accesses username
    jsonLocation = data['coordinates']
    print "TYPE" + str(type(jsonLocation))
    print "LOCATION: " + str(jsonLocation)
    doc = Document()
    #added fields
    doc.add(TextField("tweet", jsonText, Field.Store.YES))
    doc.add(TextField("u_name", jsonName, Field.Store.YES))
    # doc.add(TextField("date", jsonDate, Field.Store.YES))

    # print jsonText
    return doc

def getDirectory():
    directory = RAMDirectory()
    return directory

def index():
    # Initialize lucene and the JVM
    lucene.initVM()
    GLOBALDIRECTORY = getDirectory()
    print type(GLOBALDIRECTORY)
    print GLOBALDIRECTORY


    #Indexwriter config
    analyzer = StandardAnalyzer()
    analyzer = LimitTokenCountAnalyzer(analyzer, tokenCount)
    config = IndexWriterConfig(analyzer)
    writer = IndexWriter(GLOBALDIRECTORY, config)

    fileNames = getTxtFile(textfileDirectory) #creates document for each tweet
    for file in fileNames:
        data = getData(file)
        print file
        for tweets in data:
            doc = createDocument_tweet(tweets)
            writer.addDocument(doc) # add the document to  IndexWriter
    print "\nNumber of indexed documents: %d" % writer.numDocs() #number of documents indexed for testing
    writer.close()
    print "Indexing done!\n"
    print "------------------------------------------------------"
    return GLOBALDIRECTORY
# index()
