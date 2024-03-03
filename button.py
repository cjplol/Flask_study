from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def show_button_index():
    return render_template("button.html")

@app.route('/index.html')
def show_index():
    return render_template('button_index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2145)