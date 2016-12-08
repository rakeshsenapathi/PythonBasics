from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the homepage from:%s" % request.method


@app.route('/about')
def about():
    return "<a href='https://rakeshsenapathi.quora.com'>About Us</a>"

# for variable field in url


@app.route('/profile/<username>')
def username(username):
    return "Hi there %s" % username

# specify data type in case of int


@app.route('/post/<int:post_id>')
def post(post_id):
    return "Post id : %d" % post_id

# POST method


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if(request.method == "POST"):
        return "You came here by using POST"
    else:
        return "You used GET method"


if(__name__ == "__main__"):
    app.run(debug=True)
