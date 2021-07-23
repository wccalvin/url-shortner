import json
import os.path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/given-url", methods=["GET", "POST"])
def given_url():
    if request.method == "POST":
        new_urls = {}
        short_name = request.form["code"]
        new_urls[short_name] = {"url": request.form["url"]}
        if os.path.exists("urls.json"):
            with open("urls.json") as urls_file:
                urls = json.load(urls_file)
                if short_name in urls.keys():
                    return redirect(url_for("index"))
        with open("urls.json", "a") as url_file:
            json.dump(new_urls, url_file)
        return render_template("given_url.html", code=request.form["code"])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
