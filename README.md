# Haiku4Twitter
==================
HaiKu4Twitter is an application which was build as an project for one of the coursework naming "Digital poetics and Data Mining".


How It Works
---------------
Our project is a game in which arrow keys control a ball as it rolls through seven rotating boxes, each of which represents an emotion. When the ball hits any of the boxes, then the emotion related to that box and a syllable value (5 or 7) is sent to backend, where a tweet containing that emotion and also satisfying that syllable value is filtered, using the standard Twitter API.Three alternative hits generate a Haiku, which is displayed in the frontend. This collaboration allows users to generate Haiku based on emotional registers in the form of a simple game.

Building
------------
For running the backend server you need to install many different python libraries mentioned below 

* Python 2.7
* Import nltk (http://www.nltk.org/install.html)
   * Once you install you need to download the important cmu corpused that is required for finding syllables from the word.For  further inf     ormation go through the following web link
	   *http://www.nltk.org/data.html
* Import tweepy (pip install tweepy).This is required for filtering out tweets 
* Import tornado (pip install tornado).This is required for creating websockets to send and receive data to html pages 


For running Front end you need to have unity web player installed on your computer.Once you load the html page if unity web player 
is not present it will automatically  asked to install if not  supported by the browser.

Steps 
----------

 * Our application is supported for kind of browsers and all OS .But use windows and internet explorer as browser for avoiding any unknown issues.
* Execute first the python file (Server.py) as a backend server which will also send out the 
* For the Front End open the Build2.7.html file in the web browser.
* Play the game using keyboard arrow key .
* For any issue(web connection or if Haiku does not get displayed in the front end  ) check the backend server .

 



