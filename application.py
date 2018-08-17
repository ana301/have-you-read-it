import os

from flask import Flask, session,render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
app = Flask(__name__)



# Set up database
engine = create_engine("postgres://gndvwukxnivizg:7ba4d9097ef92d14270760f382acd1c2af8de734731d491a0283fbaa5cc6abb5@ec2-54-225-76-201.compute-1.amazonaws.com:5432/d36ql2rta4o6nn")
db = scoped_session(sessionmaker(bind=engine))


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Check for environment variable
# if not os.getenv("postgres://gndvwukxnivizg:7ba4d9097ef92d14270760f382acd1c2af8de734731d491a0283fbaa5cc6abb5@ec2-54-225-76-201.compute-1.amazonaws.com:5432/d36ql2rta4o6nn"):
#     raise RuntimeError("DATABASE_URL is not set")


res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "EmwPNJh8Z1OaV1gPm8qw", "isbns": "9781632168146"})
print(res.json())

@app.route("/")
def index():
	if not session.get("user_id") is None:
	  return render_template("home.html",user_id=user_id)

	return render_template("sign.html")

@app.route("/log_in",methods=["POST"])
def log_in():
	if session.get("user_id") is None:
		session["user_id"]=request.form.get("id")
        
    id=session.get(user_id)
    user=User.query.