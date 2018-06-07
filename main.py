from indexer import *
from searcher import *

GLOBALDIRECTORY = index()
print GLOBALDIRECTORY

# Create a searcher for the above defined RAMDirectory
searcher = IndexSearcher(DirectoryReader.open(GLOBALDIRECTORY)) #dont really know what this is either

# Create a new retrieving analyzer
analyzer = StandardAnalyzer() #dont really know what this is either

# ... and start searching!
results = []
while loopVar:
    results = search(searcher, analyzer, GLOBALDIRECTORY) #keepsearching till enter
    print results
    
