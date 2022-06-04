from flask import render_template,redirect,url_for,flash,get_flashed_messages
from app.main import app,db
from app.models import Task
from datetime import datetime

import app.forms as forms

@app.route('/')
def initial():
    return "<h1>Hello </h1>world!"

@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html',name="Vivek",tasks=tasks)


@app.route('/add',methods=['GET','POST'])
def add():
    form = forms.AddTaskFrom()
    if form.validate_on_submit():
        t = Task(task=form.task.data,
            date=datetime.utcnow())
        print(form.task.data)
        db.session.add(t)
        db.session.commit()
        flash('Task Added to the DataBase')
        return redirect(url_for('index'))
    return render_template('add.html',form=form)

@app.route('/edit/<int:task_id>',methods=['GET','POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form  = forms.AddTaskFrom()

    if task:
        if form.validate_on_submit():
            task.task = form.task.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been Updated')
            form.task.data = task.task
            return redirect(url_for('index'))
        return render_template('edit.html',form=form,task_id=task_id)
    else:
        flash('Task Not Found')
    return redirect(url_for('index')) 


@app.route('/delete/<int:task_id>',methods=['GET','POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form  = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))

        return render_template('delete.html',form=form,task_id=task_id,
        task=task.task)
    else:
        flash('Task Not Found')
    return redirect(url_for('index')) 