from flask import Flask, render_template # import flask library
# here "falsk"=Library and "Flask"= Flask class object and "render_template" is also a class object

app=Flask(__name__)
#"__name__" is a special variable that will get as value of the name of python script

@app.route("/") # This is a Decorator. home() function return the valu to this ulr map.
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    # when we execute Python file, python Script assign the name main to the file
    #thats mean: __name__ == "__main__"
    #but when we import "script1.py"  into another script then:  __name__ == "script1_"
    app.run(debug=True)
