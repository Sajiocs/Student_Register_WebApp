from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def main_page():
    return  render_template("index.html")

@app.route("/contact")
def contact_page():
    return  render_template("contact.html")

@app.route("/login")
def login_page():
    return render_template("login.html")



if __name__=="__main__":
    app.run(debug=True)