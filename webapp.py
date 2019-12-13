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
      

    
@app.route("/InfoAvailable")
def response_get_basic_info(): 
    basic_info = request.args['title'] 
    with open('classics.json') as classics_data:
         info = json.load(classics_data)
    for data in info:
        if basic_info == data['bibliography']['title']:
            Book = data['bibliography']['title']
            response = data['bibliography']['author']['name'] 
            birth = data['bibliography']['author']['birth']
            death = data['bibliography']['author']['death']
            subject = data['bibliography']['subjects']
            downloads = data['metadata']['downloads']
            link = data['metadata']['url']
            
    for data in response:
        return render_template('InfoAvailable.html', responseFromServer = Book, responseFromServer2 = response, options = get_title_options(info), responseFromServer3 = birth, responseFromServer4 = death, responseFromServer5 = subject, responseFromServer6 = downloads, responseFromServer7 = link)
        
 
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
            book = data['bibliography']['title']
            response = data['bibliography']['publication']['month name'] + " " + str(data['bibliography']['publication']['day']) + "," + str(data['bibliography']['publication']['year'])
            words = str(data['metrics']['statistics']['words'])
            formatsN = str(data['metadata']['formats']['total'])
            formats = data['metadata']['formats']['types']
            Cclassification = data ['bibliography']['congress classifications']
            
    for data in response:
        return render_template('StillCurious.html',responseFromServer8 = book, responseFromServer9 = response, options = get_title_options(info), responseFromServer10 = words, responseFromServer11 = formatsN, responseFromServer12 = formats, responseFromServer13 = Cclassification)
    
@app.route("/congressclassification")
def congressclassification():
    with open('classics.json') as classics_data:
        info = json.load(classics_data)
    return render_template('TypesOfBook.html', types = booktypes(info))

def booktypes(info):
    listOfTypes = []
    for data in info:
        if not (data ['bibliography']['congress classifications'] in listOfTypes):
            listOfTypes.append (data['bibliography']['congress classifications'])
    types = ''
    
    for data in listOfTypes:
        types = types + Markup('<a class="dropdown-item" href="#">' + data + '</a>')
    return types
 
@app.route("/Books") 
def bookTiles():
    cc_Books = request.args['congress classifications']
    with open ('classics.json')as classics_data:
        info = json.load(classics_data)
    for data in info:
        if cc_Books == data['bibliography']['congress classifications']:
            books = data['bibliography']['title']
            
    for data in response:
        return render_template('TypesOfBook.html', responseFromServer14 = books)
    
    
    
    
    
@app.route("/jsonInfo")
def render_page1():
    return render_template('InfoAvailable.html')
    
@app.route("/EvenMoreInfo")
def render_page2():
    return render_template('StillCurious.html')

@app.route("/congressclassification")
def render_page3():
    return render_template('TypesOfBook.html')
 
 
if __name__=="__main__":
    app.run(debug=False, port=54321)
