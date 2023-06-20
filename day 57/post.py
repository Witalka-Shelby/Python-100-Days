import requests

URL = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        pass

    def get_blog_post(self, id):
        blog_posts = requests.get(URL).json()

        for blog_post in blog_posts:
            if blog_post["id"] == id:
                return blog_post
        else:
            return None