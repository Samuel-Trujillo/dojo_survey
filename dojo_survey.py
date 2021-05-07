from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

from flask import Flask, render_template, request, redirect
@app.route('/result', methods= ['POST'])
def sumbit_result():
    name_form= request.form['name']
    dojo_form= request.form['dojo']
    language_form= request.form['language']
    comment_form= request.form['comment']
    return render_template("show.html", name_show=name_form, dojo_show=dojo_form, language_show=language_form,comment_show=comment_form)
if __name__ == "__main__":
    app.run(debug=True)
