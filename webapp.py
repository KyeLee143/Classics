from flask import Flask, url_for, render_template, request, Markup
import os 
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
    
    
@app.route("/jsonInfo")
def bookInfo():
    with open('classics.json') as classics_data:
        info = json.load(classics_data)
    return render_template('InfoAvailable.html', options = get_title_options(info))
                                                     
"""@app.route("/EvenMoreInfo")
def titleInfo():
    with open('classics.json') as classics_data:
        info = json.load(classics_data)
    return render_template('StillCurious.html', options = get_title_options(info))"""
    
@app.route("/response")
def response():
    with open('classics.json') as classics_data:
        info = json.load(classics_data)
    return render_template('response.html', options = get_title_options(info))
                                                     
def get_title_options(info):
        listOfTitles = []
        for data in info:
            if not (data ['bibliography']['title'] in listOfTitles):
                listOfTitles.append (data['bibliography']['title'])
        options = ''
        for data in listOfTitles:
            options = options + Markup("<option value=\"" + data + "\">" + data + "</options>")
        return options
    
"""def response_basicInfo():
    with open('classics.json') as classics_data:
         info = json.load(classics_data)
    return render_template('response.html', dataPoint = get_basic_info(info))"""  

    
@app.route("/InfoAvailable")
def response_get_basic_info(): 
    basic_info = request.args['title'] 
    with open('classics.json') as classics_data:
         info = json.load(classics_data)
    for data in info:
        if basic_info == data['bibliography']['title']:
            response = data['bibliography']['author']['name'], data['bibliography']['author']['birth']
            
    for data in response:
        return render_template('InfoAvailable.html', responseFromServer=response, options = get_title_options(info))
        
 
@app.route("/EvenMoreInfo")
def titleInfo():
    with open('classics.json') as classics_data:
        info = json.load(classics_data)
    return render_template('StillCurious.html', options = get_title_options(info))
        
@app.route("/StillCurious")
def response_more_basic_info(): 
    more_info = request.args['title'] 
    with open('classics.json') as classics_data:
         info = json.load(classics_data)
    for data in info:
        if more_info == data['bibliography']['title']:
            response = data['publication']['month name'], data['publication']['day'], data['publication']['year']
            
    for data in response:
        return render_template('StillCurious.html', responseFromServer2=response, options = get_title_options(info))
    
    
    
    
@app.route("/jsonInfo")
def render_page1():
    return render_template('InfoAvailable.html')
    
@app.route("/EvenMoreInfo")
def render_page2():
    return render_template('StillCurious.html')

@app.route("/links")
def render_page3():
    return render_template('GreatSources.html')
 
 
if __name__=="__main__":
    app.run(debug=False, port=54321)
