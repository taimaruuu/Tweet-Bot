#retrieval dependencies

from indexer import *

from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, MultiFieldQueryParser, QueryParserBase

#searcher
results = []
def search(searcher, analyzer, directory):
    print
    print "Empty to quit."
    command = raw_input("Query: ") #raw_input for query
    if command == '':
        loopVar = False
        return

    print
    print "Searching for ", command
    parserVar = MultiFieldQueryParser(fields, analyzer)
    parserVar.setDefaultOperator(QueryParserBase.AND_OPERATOR)
    query = MultiFieldQueryParser.parse(parserVar, command)



    scoreDocs = searcher.search(query, 10).scoreDocs #number is max number of matching documents
    print "total matching documents in: " + str((len(scoreDocs)))
    counter = 0
    for scoreDoc in scoreDocs: #dont really know what this is either
        doc = searcher.doc(scoreDoc.doc)
        print "@" + doc.get("u_name") + ": " + doc.get("tweet") + " Score:" + str(scoreDocs[counter].score)
        docData = {}
        docData['u_name'] = doc.get("u_name")
        docData['tweet'] = doc.get("tweet")
        docData['score'] = str(scoreDocs[counter].score)
        results.append(docData)
        counter = counter + 1
    print
    print "\n------------------------------------------------------"
    return results
