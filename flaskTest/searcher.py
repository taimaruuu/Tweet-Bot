#retrieval dependencies


from indexer import *

from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, MultiFieldQueryParser, QueryParserBase

#searcher
results = []

def search_abstract(query):
    lucene.initVM()
    GLOBALDIRECTORY = getDirectory()

    # Create a searcher for the above defined RAMDirectory
    searcher = IndexSearcher(DirectoryReader.open(GLOBALDIRECTORY)) #dont really know what this is either

    # Create a new retrieving analyzer
    analyzer = StandardAnalyzer() #dont really know what this is either

    return search(searcher, analyzer, GLOBALDIRECTORY, query)

def search(searcher, analyzer, directory, query2):
    print
    print "Empty to quit."
    # command = raw_input("Query: ") #raw_input for query
    command = query2
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
