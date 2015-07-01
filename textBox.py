import re
import nltk

def no_beginend_clean(filename):
    fileopen = open(filename,'rw')
    text = fileopen.read()
    leader = re.findall('.*\*\*\*.*\*\*\*',text[:5000],flags=re.DOTALL)
    trail = re.findall('End of.*\*\*\*.*END OF.*\*\*\*.*',text[-20000:],flags=re.DOTALL)
    text_chopped = text.replace(leader[0],'')
    text_chopped = text_chopped.replace(trail[0],'')
    text_split = text_chopped.split()
    text_clean = ' '.join(text_split)
    return text_clean

def thousand_splitter(filename,n=1000,folder=''):
    '''given filename, strips gutenberg intro and conclusion,
    creates new numbered chunks of length n tokens, where default n value is 1000; 
    can use folder flag to specify alternate folder.'''
    text = no_beginend_clean(filename)
    tokes = nltk.tokenize.word_tokenize(text)
    start = 0
    end = n
    length = len(tokes)
    counter = 1
    while start < length - n:
        fname = filename[:-4]+'_chunk_%s.txt' % str(counter).zfill(3)
        with open(folder+fname,'w') as f:
            thousand = ' '.join(tokes[start:end])
            f.write(thousand)
        counter += 1
        start += n
        end = start + n    
    fname = filename[:-4]+'_chunk_%s.txt' % str(counter).zfill(3)
    with open(folder+fname,'w') as f:
        thousand = ' '.join(tokes[start:])
        f.write(thousand)

def only_nouns(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['NN','NNS']:
            newtokes.append(tag[0])
    return newtokes

def only_adj(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['JJ','JJR','JJS']:
            newtokes.append(tag[0])
    return newtokes

def only_conj(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['CC']:
            newtokes.append(tag[0])
    return newtokes

def only_det(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['DT']:
            newtokes.append(tag[0])
    return newtokes

def only_prep(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['IN']:
            newtokes.append(tag[0])
    return newtokes

def only_adv(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['RB','RBR','RBS']:
            newtokes.append(tag[0])
    return newtokes

def only_verbs(filename):
    with open(filename,'r') as f:
        text = f.read()
    tokes = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokes)
    newtokes = []
    for tag in tagged:
        if tag[1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
            newtokes.append(tag[0])
    return newtokes

def wordLength(myText):
    """Cleans text of caps and punctuation; 
    splits words; 
    creates list of word lengths; 
    creates dictionary of word-length values & their frequencies"""
    
    lengthDict = {}
    allLengths = []
    puncMarks = [',', '.', '?', '!', ':', ';', '\'', '\"', '(', ')', '[', ']', '-']
    for item in puncMarks:
            myText = myText.replace(item, '')
    lowerText = myText.lower()
    textWords = lowerText.split()
    
    ## Create list of word lengths
    for word in textWords:
        length = len(word)
        allLengths.append(length)
    
    ## Make dict of word lengths & freqs
    for length in allLengths:
        if length in lengthDict:
            lengthDict[length] += 1
        else:
            lengthDict[length] = 1
    
    return lengthDict

    ##note: I am defining a word-splitting and cleaning function here for later use
def wordSplitClean(myText,lower=True):
    puncMarks = [',', '.', '?', '!', ':', ';', '\'', '\"', '(', ')', '[', ']', '-']
    for item in puncMarks:
            myText = myText.replace(item, '')
    if lower:
        lowerText = myText.lower()
    textWords = lowerText.split()
    return textWords


def LFDLenFreqCorr(myText):
    """spit out lengths and freqs; convert to arrays and calc corr; 
    spit out corrcoef"""
    
    ##hey Graham is it kosher to import within a function or is that bad form?
    import numpy

    lenFreqDict = wordLength(myText)
    LFDLengths = lenFreqDict.keys()
    LFDFreqs = lenFreqDict.values()

    ##first output
    print LFDLengths
    print LFDFreqs

    ##convert to arrays and find corrcoef
    LFDLenArray = numpy.array(LFDLengths)
    LFDFreqArray = numpy.array(LFDFreqs)
    LFDLenFreqCorr = numpy.corrcoef(LFDLenArray, LFDFreqArray)
    
    ##indexed to return only corrcoef
    return LFDLenFreqCorr[0][1]


def length_z_score(givenWord, fullText):
    ## your code here
    
    allLengths = []
    givenWordLen = len(givenWord)
    ##WSC function defined above
    textWords = wordSplitClean(fullText)
    
    ##average length
    for word in textWords:
        allLengths.append(len(word))
    avgLength = float(sum(allLengths)/len(allLengths))
    
    ##standard deviation (dists from mean squared plugged into sd formula)
    distsFromMeanSq = []
    for x in allLengths:
        distsFromMeanSq.append((x-avgLength) ** 2)
    stDev = (sum(distsFromMeanSq)/len(allLengths)) ** (.5)
    
    ## z-score = distance from avgLength / standard deviation
    z_score = (givenWordLen-avgLength)/stDev
    
    return z_score


def twoTextSets(firstText, secondText):
    """wordlist texts; wordlists to set; outputs using set methods"""
    
    ## clean and make word list
    textWordsOne = wordSplitClean(firstText)
    textWordsTwo = wordSplitClean(secondText)
    
    setOne = set(textWordsOne)
    setTwo = set(textWordsTwo)
    
    print ("All words in Text 1 and Text 2: " + str(list(setOne.union(setTwo)))) + "\n"
    print "Words common to Text 1 and Text 2: " + str(list(setOne.intersection(setTwo))) + "\n"
    print "Words unique to Text 1: " + str(list(setOne.difference(setTwo))) + "\n"
    print "Words unique to Text 2: " + str(list(setTwo.difference(setOne)))
  

def distinctRat(givenWord, firstText, secondText):
    ##make word lists and calculate Dist. Ratio
    textWordsOne = wordSplitClean(firstText)
    textWordsTwo = wordSplitClean(secondText)
    oneCount = textWordsOne.count(givenWord)
    twoCount = textWordsTwo.count(givenWord)
    dRat = float(oneCount+1)/float(twoCount+1)
    return dRat

def normalDistinctRat(givenWord, firstText, secondText):
    ##make word lists and calculate Dist. Ratio
    textWordsOne = wordSplitClean(firstText)
    textWordsTwo = wordSplitClean(secondText)
    oneCount = textWordsOne.count(givenWord)
    twoCount = textWordsTwo.count(givenWord)
    oneCountNorm = float(textWordsOne.count(givenWord))/float(len(textWordsOne))
    twoCountNorm = float(textWordsTwo.count(givenWord))/float(len(textWordsTwo))
    dRatNorm = float(oneCountNorm+1)/float(twoCountNorm+1)
    return dRatNorm

def dRatRace(firstText,secondText):
    '''use distinctRat function above to make list of tuples of word and dRat, sort list on dRat'''
    textWordsOne = wordSplitClean(firstText)
    drat_list = [ (word, distinctRat(word,firstText,secondText)) for word in textWordsOne ]
    ##note use of "set" to eliminate duplicates
    drat_sorted_list = sorted(list(set(drat_list)),key=lambda x: x[1], reverse=True)
    
    return drat_sorted_list

def bigramCount(myText):
    """make bigrams, count instances of each, zip into dictionary (eliminates duplicates en route)"""
    bigrams = []
    words = wordSplitClean(myText)
    ## note that we need to use enumerate or an index counter to avoid unwanted duplicates
    for ndx, word in enumerate(words[:-1]):
        bigrams.append((words[ndx-1],words[ndx]))
    
    ##this alternative produced duplicates but is commented for reference later:
    #bigrams = [ (word, words[words.index(word)+1]) for word in words[:-1] ]
   
    bgCounts = [ bigrams.count(tup) for tup in bigrams ]
    freqsBigram = dict(zip(bigrams,bgCounts))
    
    return freqsBigram

def bicharCount(myText):
    bichars = []
    words = myText.lower().split()
    chars = ''.join(words)
    
    ## note that we need to use enumerate or an index counter to avoid unwanted duplicates
    for ndx, char in enumerate(chars[:-1]):
        bichars.append((chars[ndx],chars[ndx+1]))
   
    bcCounts = [ bichars.count(tup) for tup in bichars ]
    freqsBichar = dict(zip(bichars,bcCounts))

    return freqsBichar


def ngramCount(ngramInt,myText):
    """make ngrams of length ngramInt, count instances of each, zip into dictionary"""
    ngrams = []
    words = wordSplitClean(myText)
    ## note that we need to use enumerate or an index counter to avoid unwanted duplicates; here using ngramInt value to specify length of tuple returned, executed via list slice and (ndx+ngramInt)
    for ndx, word in enumerate(words[:-(ngramInt-1)]):
        ngrams.append(tuple(words[ndx:(ndx+(ngramInt))]))
    ##this alternative produced duplicates but is commented for reference later:
    #bigrams = [ (word, words[words.index(word)+1]) for word in words[:-1] ]
   
    ngCounts = [ ngrams.count(tup) for tup in ngrams ]
    freqsNgram = dict(zip(ngrams,ngCounts))
    
    return freqsNgram

def ncharCount(ncharInt,myText):
    """make nchar of length ncharInt, count instances of each, zip into dictionary"""
    nchars = []
    words = myText.lower().split()
    chars = ''.join(words)
    ## note that we need to use enumerate or an index counter to avoid unwanted duplicates; here using ngramInt value to specify length of tuple returned, executed via list slice and (ndx+ngramInt)
    for ndx, char in enumerate(chars[:-(ncharInt-1)]):
        nchars.append(tuple(chars[ndx:(ndx+(ncharInt))]))
   
    ncCounts = [ nchars.count(tup) for tup in nchars ]
    freqsNchar = dict(zip(nchars,ncCounts))
    
    return freqsNchar