from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={
        "name":request.form.get("name"),
        "roll":request.form.get("roll"),
        "email":request.form.get("email"),
        "phno":request.form.get("phno"),
        "dept":request.form.get("dept"),
        "event":request.form.get("event"),
        }
        return render_template("formresult.html",data=data)
    return render_template("event registration.html")
if __name__=='__main__':
    app.run(debug=True)