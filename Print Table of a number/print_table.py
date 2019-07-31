from flask import Flask, render_template, request

app=Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST":
        return render_template("printTable.html",num=int(request.form.get("numberInputFromForm")))
    return render_template("index.html")
