from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        data={
        "name":request.form.get("name"),
        "email":request.form.get("email"),
        "password":request.form.get("pwd"),
        "gender":request.form.get("gender"),
        "interests":request.form.get("interests"),
        "country":request.form.get("country"),
        "comments":request.form.get("comments"),
        "file":request.files.get("file").filename if request.files.get("file") else "No file uploaded"
        }
        return render_template("result.html",data=data)
    return render_template("form1.html")
if __name__=='__main__':
    app.run(debug=True)