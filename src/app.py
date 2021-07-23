import json

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/given-url", methods=["GET", "POST"])
def given_url():
    if request.method == "POST":
        urls = {}
        short_name = request.form["code"]
        urls[short_name] = {"url": request.form["url"]}
        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)
        return render_template("given_url.html", code=request.form["code"])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
