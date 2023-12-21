from flask import Flask                     # From the flask module import the Flask class

# OOP - Object Oriented Paradigm

app =  Flask(__name__)                      #  Create an object from the Flask class (instance)

@app.get("/")                               # Flask decorator to map routes to view functions
def index():                                # Flask view function (wrapped)
    me = {                                  # Python dictionary    
        "first_name": "Andrew",
        "last_name": "McKinnon",
        "hobbies": "Esports",
        "is_active": True
    }
    return me                               # When you return a dictionary from Flask,
                                            # it gets converted to JSON automatically.