# ##########
# @Title: Roller
# @Purpose: Absurd Daily programming challenge app that is really just a randit
# @Author: Patrick Hastings
# @Version: 0.1
# ##########

from flask import Flask, render_template
app = Flask(__name__)


# Index
@app.route('/')
@app.route('/index')
def index(challenge=0, plang=0):	
	'''
Returns the main page of the website
	'''
	return render_template('index.html', challenge=challenge, plang=plang)



