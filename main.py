from flask import Flask, render_template, request
from helper import begruessung

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            # Aufruf der Begrüßungsfunktion aus helper.py
            message = begruessung(name)
            return render_template('index.html', message=message)
    return render_template('index.html', message=None)

if __name__ == '__main__':
    app.run(debug=True)
