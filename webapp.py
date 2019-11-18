from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
    
@app.route("/InfoAvailable")
def InfoAvailable():
    with open('classics.json') as classics_data:
        titles = json.load(classics_data)
    return render_template('InfoAvailable.html', options = get_title_options(titles))
                           
def get_title_options(titles):
    listOfTitles = []
    for data in titles:
        if not (data ['title'] in listOfTitles):
            listOfStates.append (data['title'])
    options = '' 
    for data in listOfTitles:
        options = options + Markup("<option value=\"" + data + "\">" + data + "</options>")
    return options
    
    
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
