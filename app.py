import os

from flask import Flask, redirect, url_for
from entries import bp as entries_bp
from db import init_app

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'journal.db'),
)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

init_app(app)
app.register_blueprint(entries_bp)

@app.route('/')
def root():
    return redirect(url_for('entries.home'))

if __name__ == '__main__':
    app.run(debug=True)
