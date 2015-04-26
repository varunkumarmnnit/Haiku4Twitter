import json
import sys
import os
def main():
    
    tweet_file = open(sys.argv[1])
    histogram = {}
    total_terms = 0
    for line in tweet_file:
       tweet = json.loads(line)
        if 'text' in tweet:
        tweet_mod = tweet['text'].encode('ascii', 'ignore')
        tweet["text"] = os.linesep.join([s for s in tweet["text"].splitlines() if s])
        words = tweet["text"].split(" ")
        for term in words:
                flg = "\n" in term
                if term != "" and flg != True:
                    print term
                    print flg
                    total_terms += 1
                    if histogram.has_key(term):
                        histogram[term] += 1
                    else:
                        histogram[term] = 1
    for key in histogram.iterkeys():
        histogram[key] = float(histogram[key])/float(total_terms)
        print key, histogram[key]

    #print histogram.keys()
    #print type(histogram.keys()[0])
    #print type(histogram.values()[0])   
    


if __name__ == '__main__':
    main()            
    
