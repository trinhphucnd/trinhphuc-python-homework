from flask import Flask , render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    return render_template('index.html') 


@app.route('/school')
def school():
  return redirect("https://mindx.edu.vn", code=302)

if __name__ == '__main__':
  app.run(debug=True)
 
