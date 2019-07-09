from flask import Flask, render_template, request
from data import *

#from flask_basic.data import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    print("app.py:  ")

    if request == None:
        return render_template('home.html')
    elif request.method == 'POST':
        if request.form.get('auth_checkbox') and request.form.get('capture_checkbox'):
            print("Both checkboxes selected")
            result = request.form
            config = getConfig(result)
            auth = processAuth(result, config)
            capture= processCapture(result, config)
            return render_template('home.html', auth=auth,capture=capture)
        elif request.form.get('auth_checkbox'):
            print("Auth checkbox selected")
            result = request.form
            config = getConfig(result)
            auth = processAuth(result, config)
            return render_template('home.html', auth=auth)
        
        elif request.form.get('capture_checkbox'):
            print("Capture checkbox selected")
            result = request.form
            config = getConfig(result)
            capture = processCapture(result, config)
            return render_template('home.html', capture=capture)
            
        return render_template('home.html')

    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html') 

     
if __name__ == '__main__':
    app.run(debug=True)