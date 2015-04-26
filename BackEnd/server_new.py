# Hello World program in Python
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import time
# twitter client
import tweepy
import json
import re
import os
import sys
 
# natural language toolkit for syllable countin
import nltk
from nltk.corpus import cmudict
 
# digit detection
#import curses
#from curses.ascii import isdigit
syl_g_count=0
emotion_file=0
str_result = 0
ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words('english'))
NON_ENGLISH_STOPWORDS = set(nltk.corpus.stopwords.words()) - ENGLISH_STOPWORDS
my_value=0 
consumer_key = 'WkAE72PmL5oUW9CaBSkQ9cuBr'
consumer_secret = 'aU9aBn34FQR3c9ReFkA6ShDwULDuvspR0ZDckqSOBoNYmBJjRn'
access_token = '3146099230-v3Z5XmRUcc02rrvOmX6yelSL5Y4DmTQLf9boKk3'
access_token_secret = '7wcdGkoPPZzrk8nLDyTa0rXE8YJ3X2UkFYjKlJyC2DfuR'

def is_english(text):
#    print "Tweet Found %s\n\n " % text
    text = text.lower()
    words = set(nltk.wordpunct_tokenize(text))
    return len(words & ENGLISH_STOPWORDS) > len(words & NON_ENGLISH_STOPWORDS)


def is_haiku(text):
    
    text_orig = text
    text = text.lower()
    #if filter(str.isdigit, str(text)):
    #    return False
    words =  nltk.wordpunct_tokenize(re.sub('[^a-zA-Z_ ]', '',text))
    global syl_g_count
    global emotion_file
    global str_result
    count = 0
    syl_count = 0
    word_count = 0
    haiku_line_count = 0
    lines = []
    lines_tmp = []
    text_word = words[0].lower()
    d = cmudict.dict()
    if ':' in words:
       i = words.index(':') + 1
    else:
      i=0
    for word in words[i:]:
     if word == ':' or  word == '.' or  word == '@' or word == '#':
       continue
     if word.lower() not in d:
       return False
     else:
        p = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]][0]
        syl_count += p
        lines_tmp.append(word)
        if syl_count == syl_g_count:
                lines.append(lines_tmp)
                str_result = ' '.join(lines_tmp)
                print "%s\n" % str_result
                lines_tmp = []
                syl_count = 0
                count = count+1
                return True
        else:
            continue;
 
     
    else:
        return False

def __init__(self, api=None):
     super(StreamWatcherListener, self).__init__()
     self.num_tweets = 0
 
class StreamWatcherListener(tweepy.StreamListener):
   def on_data(self, data):
        jsonData=json.loads(data)
        if 'text' in jsonData:
             text=jsonData["text"].encode('ascii','ignore')
             text=os.linesep.join([s for s in text.splitlines() if s])
             if is_english(text):
                  if  is_haiku(text):
                            #  print "\n  user info : %s %s" %(jsonData["created_at"], jsonData["source"],)
                              return False
                  else:
					   return True 
 
   def on_error(self, status_code):
      print "An error has occurred! Status code = %s" % status_code
      return True  # keep the dream alive

 


 
class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
     return True
	
    def open(self):
        print 'new connection'
        #self.write_message("Hello World!")

         	
      
    def on_message(self, message):
        print 'message received %s' % message
        global syl_g_count
        global emotion_file
        final_lines = []
        final_lines = message.split()
        syl_g_count = int(final_lines[1])
        emotion_file=str(final_lines[0])
        l = StreamWatcherListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = tweepy.Stream(auth, l)
        stream.filter(track=[emotion_file])
        self.write_message( str_result)
        #print 'received:', message

 
    def on_close(self):
      print 'connection closed'
 
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9090)
    tornado.ioloop.IOLoop.instance().start()
