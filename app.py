from flask import Flask,request
from emails import get_mars_photo,send_mars_email

app = Flask(__name__)

app.route('/email',methods = ['POST'])
def email_response():
    to_email = request.form['to']
    from_email = request.form['from']
    text = request.form['text']

    sol = str.split(text)[0]

    if sol.isdigit():
        img_url = get_mars_photo(sol)
    else:
        img_url = get_mars_photo(1000)
    
    send_mars_email(from_email,to_email,img_url)
    return '',200



if __name__ == '__main__':

    app.run(debug = True)
