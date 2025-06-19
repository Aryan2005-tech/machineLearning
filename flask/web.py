from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return '<h1>Hello world! </h1>'
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.form  # Get form data
        return f"Received data: {data}"
    return render_template("form.html")

if __name__=='__main__':
    app.run(debug=True)