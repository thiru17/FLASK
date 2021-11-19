import pandas as pd
from time import sleep
from flask import Flask, render_template, send_file

# csv to html table conversion and save the output to inside templates folder
csv = pd.read_csv("csvout.csv")
csv.to_html("templates/htmlout.html")

#file1 = open("templates/htmlout.html", "a")  # append mode
#file1.write("\n <form action='csvout.csv'><input type=submit value=DOWNLOAD></input></form> ")
#file1.close()

# put sleep some seconds because of output file saving process
sleep(2)

# start flask
app = Flask(__name__)

@app.route("/")
def home():
	return (render_template("htmlout.html") + "<form action='/downloa'><input type=submit value=DOWNLOAD></input></form>" )
	
@app.route('/downloa')
def downloadFile ():
    
    path = "/home/thiru/NECURITY/flask/csvout.csv"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
	app.run(debug=True)
