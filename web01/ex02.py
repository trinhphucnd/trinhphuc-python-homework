from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    users = {
    "phuc" : {"name" : "Trinh Hong Phuc",
              "age": 23},
    "quy"  : {"name": "Dinh Xuan Quy",
             "age" : 20}
}
    for u in users :
        if username == u :
            return render_template("users.html",users = users , username = username)

if __name__ == "__main__":
    app.run(debug =True)