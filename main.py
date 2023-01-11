from flask import Flask, Response, render_template, request
from flask.templating import render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    css="static/css/main.css"
    return render_template('index.html',css=css)
   
@app.route('/lostmine', methods=['GET','POST'])
def lostmine():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Lost Mine of Phandelver"
    background="static/lost_mine.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/madmage', methods=['GET','POST'])
def madmage():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Dungeon of the Mad Mage"
    background="static/mad_mage.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/tomb', methods=['GET','POST'])
def tomb():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Tomb of Annihilation"
    background="static/mad_mage.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/undercity', methods=['GET','POST'])
def undercity():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Undercity"
    background="static/undercity.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/monarch', methods=['GET','POST'])
def monarch():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Monarch"
    background="static/monarch.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/initiative', methods=['GET','POST'])
def initiative():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Initiative"
    background="static/initiative.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)

@app.route('/blood', methods=['GET','POST'])
def blood():
    css="static/css/main.css"
    dot="static/dot.js"
    title="Blood"
    background="static/blood.png"
    return render_template('dungeon.html',css=css,title=title,background=background,dot=dot)



if __name__ == "__main__":
    #    app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
