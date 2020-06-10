from flask import Flask, render_template
app = Flask(__name__)

# Input your blog posts here
posts = [
    {
        # Repeat this for each blog post
        "title": "Insert text here",
        "author": "Optional.",
        "description": "Insert text here"
    },
    {
        # Repeat this for each blog post
        "title": "Insert text here",
        "author": "Optional.",
        "description": "Insert text here"
    },
]

@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html", myposts=posts)

if __name__ == "__main__":
    app.run(debug=True)