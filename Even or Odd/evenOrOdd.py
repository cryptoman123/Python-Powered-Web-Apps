from flask import Flask, render_template, request

app=Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method=="POST":
        num=int(request.form.get("numberInputFromForm"))
        dict={'even':False, 'odd':False, 'zero':False, 'number_input':num}
        if num==0:
            dict['zero']=True
        elif num%2==0:
            dict['even']=True
        else:
            dict['odd']=True
        return render_template("evenOrOdd.html", dict=dict)
    return render_template("index.html")
