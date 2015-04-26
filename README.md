# Haiku4Twitter
==================
HaiKu4Twitter is an application which was build as an project for one of the coursework naming "Digital poetics and Data Mining".


How It Works
---------------
It is a game in which a ball will be rolling and there are seven rotationg boxes.Each of the box is representing an emotion .The movement of the ball could be controlled by the user using the arrow key from the keyboard.When the ball hits any of the boxes then the emotion related to that box and a syllable value (5 or 7 ) is sent to backend .In the backend a  tweet is filtered out  involving that emotion and also satisfying that syllable value using the standard twitter API.Three alternative hits generate an Haiku and displayed in the FrontEnd .So this allows users to generate Haiku based on the emotion in the form of a simple game .

Building
------------
For running the backend server you need to install many different python libraries mentioned below 

1) Python 2.7
2) Import nltk (http://www.nltk.org/install.html)
    Once you install you need to download the important cmu corpused that is required for finding syllables from the word.For  further infom    ration got through the following web link
	http://www.nltk.org/data.html
3) Import tweepy (pip install tweepy).This is required for filtering out tweets 
4) Import tornado (pip install tornado).This is required for creating websockets to send and receive data to html pages 

For running Front end you need to have unity web player installed on your computer.Once you load the html page if unity web player 
is not present it will automaticaaly asked to install if not  supported by the browser.

#####Steps 
 Our application is supported for kind of browsers and all OS .But use windows and internet explorer as browser for avoiding any unknown issues.
Execute first the python file (server_new.py) as a backend server
 



