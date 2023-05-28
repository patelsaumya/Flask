from flask import Flask, render_template

app = Flask(__name__)

# Execute this function for 'GET' request (default)
@app.route('/')
def index():
    # View Function
    name = "Peter"
    numbers = [1,2,3,4,5]
    pup_dictionary = {'pup_name': 'Batman'}
    return render_template('basic.html', name=name, numbers=numbers, pup_dictionary=pup_dictionary)

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

# Dynamic Route
@app.route("/puppy/<name>")
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name)

@app.route('/puppy_name/<name>')
def puppylatin(name):
    pupname = ''
    if name[-1] == 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    return "<h1>Your puppy latin name is: {}</h1>".format(pupname)

if __name__ ==  "__main__":
    app.run()