from flask import Flask, render_template,request
import google.generativeai as palm
import os

app = Flask(__name__)

api = os.getenv("MAKERSUITE_API_TOKEN")

model = {"model": "models/chat-bison-001"}

palm.configure(api_key="AIzaSyCI__rHRL-O4Frz6u21NO-mZzMUF8_G7aQ")

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/genAI",methods=["GET","POST"])
def genAI():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("genAI.html",r=r.last))
    
if __name__ == "__main__":
    app.run()
