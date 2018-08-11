from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('home.html'), "html home page"

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=False, threaded=True)