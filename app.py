import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL
from flask_table import Table, Col

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:andrei123@localhost/unicorns'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Unicorn(db.Model):

    __tablename__ = 'Unicorns'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Unicorn name: {self.name}"

class Results(Table):
    classes = ['table', 'table-striped', 'table-bordered', 'table-condensed','table table-hover']
    id = Col('Id')
    name = Col('Name')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET','POST'])
def add_unicorn():
    form=AddForm()
    if form.validate_on_submit():
        name=form.name.data
        new_unicorn=Unicorn(name)
        db.session.add(new_unicorn)
        db.session.commit()
        return redirect(url_for('list_unicorn'))
    return render_template('add.html',form=form)

@app.route("/list_unicorn")
def list_unicorn():
        unicorns = Unicorn.query.all()
        table=Results(unicorns)
        table.border=True
        return render_template('list.html', table=table)

@app.route('/delete', methods=['GET','POST'])
def delete_unicorn():
        form=DelForm()
        if form.validate_on_submit():
            id=form.id.data
            unicorn=Unicorn.query.get(id)
            if unicorn == None:
                flash("This unicorn doesn't exist! Please Type another ID.")
            else:
                db.session.delete(unicorn)
                db.session.commit()
                return redirect(url_for('list_unicorn'))
        return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
