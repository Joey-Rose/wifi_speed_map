from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/free_ookla')
def free_ookla(variable):
    return "hello world"

@app.route('/mb')
def mb():
    return render_template('mapbox.html')

@app.route('/mb2')
def mb2():
    return render_template('other_mapbox.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
