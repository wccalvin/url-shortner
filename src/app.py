import csv
import os.path

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/given-url", methods=["GET", "POST"])
def given_url():
    if request.method == "POST":
        short_name = request.form["code"]
        url = request.form["url"]
        if os.path.exists("urls.csv"):
            with open("urls.csv", newline="") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                short_names = [i[0] for i in csv_reader]
                if short_name in short_names:
                    flash(f"{short_name} is taken. Provide another short name.")
                    return redirect(url_for("index"))
        with open("urls.csv", "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([short_name, url])
        return render_template("given_url.html", code=request.form["code"])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
