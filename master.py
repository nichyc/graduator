import os

import AHIget
import pprint

from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key='l10odlkashb1097';

@app.route('/')
def renderHome():
    return render_template('home.html')

@app.route('/results', methods=['GET', 'POST'])
def renderResults():
    session['requirements']='No'
    if request.form['ethno']=='ethno': 
##        session['requirements'].append('Yes')
        session['requirements']='Yes'
    return render_template('results.html')


##def ethnoGet():
##    ethno_dict = AHIget.getGE(AHIget.ethno_url)
##    pprint.pprint(ethno_dict)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
