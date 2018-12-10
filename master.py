import os

import collections
import GE
import pprint

from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key='l10odlkashb1097';

ahi_url="https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/AHICourseList.aspx"
ethno_url='https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/EthnicityCourses.aspx'

@app.route('/')
def renderHome():
    session['error'] = False
    session['URLrequirements'] = []
    return render_template('home.html')

@app.route('/results', methods=['GET', 'POST'])
def renderResults():
    if request.form.get('ahibox'):
        session['URLrequirements'].append(ahi_url)
    if request.form.get('ethnobox'):
        session['URLrequirements'].append(ethno_url)
        
    if len(session['URLrequirements']) <= 1:
        session['error'] = True
        session['URLrequirements'] = []
        return render_template('home.html')

    if len(session['URLrequirements']) >= 2:
        session['error'] = False
        session['fullList'] = list(map(GE.getGE, session['URLrequirements']))
        session['c2d'] = {}

        for r in session['fullList']:
            for c in r['Course List']:
                if c in session['c2d']:
                    session['c2d'][c].append(r['Requirement'])
                else:
                    session['c2d'][c] = [r['Requirement']]
        return render_template('results.html')
        
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)

