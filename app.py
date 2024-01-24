from flask import Flask, render_template, request, session, redirect, flash
from api_requests import get_shorter_link
import pdb
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

app = Flask(__name__, template_folder = "templates")

#GET SECRET KEY
app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['SESSION_TYPE'] = environ.get("SESSION_TYPE")

#ROUTES
@app.route('/')
def show_homepage():
    """show home page"""
    #get link and short link from session or pass none
    link = session.pop('link', None)
    shortened_link = session.pop('shortened_link', None)
    return render_template('index.html', link = link, shortened_url = shortened_link)

@app.route('/shorten_url', methods = ['GET', 'POST'])
def shorten_url():
    """get url from client side """
    if request.method == 'POST':
        link = request.form.get('link')
        shorter_link_dict  = get_shorter_link(link)

        #if link cant be gotten flash an error message, else add link and shorter link to session
        if shorter_link_dict['response'] == 'error':
            flash('Request could not be completed', 'error')
        elif shorter_link_dict['response'] == 'success':
            session['link'] = link
            session['shortened_link'] = shorter_link_dict['message']

        return redirect('/')