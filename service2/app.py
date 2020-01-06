from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def random_name():
    return ("Test")

if __name__ == '__main__':
    app.run()