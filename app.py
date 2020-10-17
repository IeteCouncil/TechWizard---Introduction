from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, template_folder='templates')
app.secret_key = 'mysecretkey'

@app.route('/')
def introduction():
    return(render_template('intro.html'))

@app.route('/story')
def storyplot():
    return(render_template('story.html'))

if __name__ == "__main__":
    app.run(debug=True)




