from flask import Blueprint, redirect, render_template, request, url_for
from db import get_db
from datetime import datetime

bp = Blueprint('entries', __name__, url_prefix='/entries')  # Added url_prefix='/entries'


@bp.route('/')
def home():
    db = get_db()
    entries = db.execute('SELECT * FROM entries ORDER BY created_at DESC').fetchall()
    return render_template('home.html', entries=entries)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        db = get_db()
        db.execute(
            'INSERT INTO entries (title, content, tags) VALUES (?, ?, ?)',
            (title, content, tags)
        )
        db.commit()
        # Updated to use 'entries.home'
        return redirect(url_for('entries.home'))
    return render_template('add.html')


@bp.route('/edit/<int:entry_id>', methods=['GET', 'POST'])
def edit(entry_id):
    db = get_db()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tags = request.form['tags']
        db.execute(
            'UPDATE entries SET title = ?, content = ?, tags = ? WHERE id = ?',
            (title, content, tags, entry_id)
        )
        db.commit()
        # Updated to use 'entries.home'
        return redirect(url_for('entries.home'))
    entry = db.execute('SELECT * FROM entries WHERE id = ?', (entry_id,)).fetchone()
    return render_template('edit.html', entry=entry)


@bp.route('/delete/<int:entry_id>', methods=['GET', 'POST'])
def delete(entry_id):
    # Handle POST request (delete entry)
    if request.method == 'POST':
        db_connection = get_db()
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM entries WHERE id = ?', (entry_id,))
        db_connection.commit()
        db_connection.close()
        return redirect(url_for('entries.home'))

    # Handle GET request (confirmation page)
    db_connection = get_db()
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM entries WHERE id = ?', (entry_id,))
    entry = cursor.fetchone()
    db_connection.close()

    return render_template('delete.html', entry=entry)
