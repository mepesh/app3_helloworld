from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/hello')
def hello_name():
    return render_template('helloworld.html')
if __name__ == '__main__':
    app.run(debug=True)
