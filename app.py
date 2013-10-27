# Abhishek Biswal
# http://abhishekbiswal.com

from flask import Flask, session, url_for, render_template, request, redirect
from flask_oauth import OAuth

oauth = OAuth()

# Set up twitter OAuth client
twitter = oauth.remote_app('twitter',
    base_url          = 'https://api.twitter.com/1/',
    request_token_url = 'https://api.twitter.com/oauth/request_token',
    access_token_url  = 'https://api.twitter.com/oauth/access_token',
    authorize_url     = 'https://api.twitter.com/oauth/authenticate',
    consumer_key      = 'YOUR_CONSUMER_KEY',
    consumer_secret   = 'YOUR_CONSUMER_SECRET'
)

# returns a tuple of twitter tokens, if they exist
@twitter.tokengetter
def get_twitter_token(token=None):
	return session.get('twitter_token')

@app.route('/login')
def login():
	return twitter.authorize(callback=url_for('oauth_authorized',
        next=request.args.get('next'), _external=True))

@app.route('/oauth_authorized')
@twitter.authorized_handler
def oauth_authorized(resp):
	next_url = request.args.get('next') or url_for('index')
	if resp is None:
		return "Error Occured."
	return str(resp) # Prints the output. From here you can either insert the info into the database or directly create a session using the info.