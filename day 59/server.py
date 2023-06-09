from flask import Flask, render_template, request
import requests

API_URL = "https://api.npoint.io/69084c9c49e83151f9ca"

blog_posts = requests.get(API_URL).json()

app = Flask(__name__, static_url_path='/static/')


@app.route("/")
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]
        # send email with all data
        # print(name + email + phone_number + message)
        return f"Successfully sent you message"
    else:
        return render_template("contact.html")


@app.route("/post/<id>")
def post(id):
    for blog_post in blog_posts:
        if blog_post["id"] == int(id):
            blog_article = blog_post
            break
        else:
            blog_article = "No new posts"
    return render_template("post.html", article=blog_article)


if __name__ == "__main__":
    app.run(debug=True)