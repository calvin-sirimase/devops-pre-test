from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome/')
@app.route('/welcome/<nama>')
def welcome(nama=None):
    return render_template('welcome.html', nama=nama)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

