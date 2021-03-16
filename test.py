from flask import Flask, url_for


app = Flask(__name__)


@app.route('/editar/<int:id>')
def editar(id):
    pass

with app.test_request_context():
    print(url_for('editar', id=5))