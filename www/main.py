from flask import Flask, render_template
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

@app.route("/")
def index():
    from model import Database, Article
    # connect to database
    db = create_engine('sqlite:///nar.db', echo=True)
    Session = sessionmaker(bind=db)
    session = Session()

    databases = []
    for database in session.query(Database):
        databases.append({'title': database.title, 'is_alive': database.is_alive})
    print databases

    return render_template('index.html', databases=databases)

if __name__ == "__main__":
    app.run()
