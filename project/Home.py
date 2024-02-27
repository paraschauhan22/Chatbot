from flask import Flask,render_template,request
import requests

#endpoint
url = "https://chatgpt-api7.p.rapidapi.com/ask"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "487f333ee7msh815a5591da21780p1ee6f2jsne9d296ff605b",
	"X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
}
x = 0
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home_page():
    global x
    if x==0:
        user = ""
    else:
        user = str(request.form['Response'])
    payload = {"query": user}
    response = requests.request("POST", url, json=payload, headers=headers)
    x += 1
    # print(f"AI: {response.json()['response']}")
    return render_template('home.html',item_name=response.json()['response'],results=request.form)



