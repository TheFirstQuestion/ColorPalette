from flask import Flask, render_template,redirect, url_for
import random
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


#### config ####
LINK_FILE = "links.txt"
SHUFFLE = True
NUM_BLOCKS = 5
################


def readFile():
    colors = []
    with open(LINK_FILE) as f:
        content = f.readlines()
    for link in content:
        firstSplit = link.split("/")[-1]
        theseColors = firstSplit.split("-")
        for color in theseColors:
            # get rid of \n
            if len(color) > 6:
                color = color[:-1]
            if not color in colors:
                for i in range(0, NUM_BLOCKS):
                    colors.append(color)
    if (SHUFFLE):
        random.shuffle(colors)
    return colors

@app.route("/")
def main():
    return render_template('index.html', COLORS=readFile())

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=302)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
