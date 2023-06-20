from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url).json()

    return render_template("index.html", posts=response)

@app.route("/post/<id>")
def get_post(id):
    blog_dic = Post().get_blog_post(int(id))
    post_title = blog_dic["title"]
    post_subtitle = blog_dic["subtitle"]
    post_body = blog_dic["body"]
    return render_template("post.html", title=post_title, subtitle=post_subtitle, body=post_body)


if __name__ == "__main__":
    app.run(debug=True)
