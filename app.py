from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(500), nullable=False)

# Initialize Database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    bookmarks = Bookmark.query.order_by(Bookmark.id.desc()).all()
    return render_template('index.html', bookmarks=bookmarks)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    url = request.form.get('url')
    if name and url:
        new_bookmark = Bookmark(name=name, url=url)
        db.session.add(new_bookmark)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    bookmark = Bookmark.query.get_or_404(id)
    bookmark.name = request.form.get('name')
    bookmark.url = request.form.get('url')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    bookmark = Bookmark.query.get_or_404(id)
    db.session.delete(bookmark)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)