from flask import render_template, flash, redirect, url_for, request
from app import app, aws, database as db
from app.forms import *
from app import config

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddStudentForm()

    if form.validate_on_submit():
        if not db.check_connection():
            flash('No database conncetion')
        else:
            try:
                if not db.get_group(form.group.data):
                    if db.create_group(form.group.data):
                        print(f'group {form.group.data} created')
                    else:
                        raise Exception(f'group {form.group.data} was not created')
                if db.create_student(form.name.data, form.group.data):
                    flash('Data inserted successfully')
                else:
                    raise Exception(f'student {form.name.data} was not created')
            except Exception as e:
                flash(e)

    try:
        students = db.get_students()
    except:
        students=None

    return render_template(
        'index.html.j2',
        title='Home',
        form=form,
        db_connection = db.check_connection().info,
        students=students
    )

@app.route('/health', methods=['GET', 'POST'])
def health():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Reload config':
            config.init_config()
            flash('Config reloaded')
        elif request.form['submit_button'] == 'Recheck S3 access':
            if aws.check_s3_access():
                flash('S3 accessed')
            else:
                flash('S3 access deined')
        elif request.form['submit_button'] == 'Reconnect to database':
            try:
                db.init_db()
                db.init_requests()
                flash('Connect successfully')
            except Exception as e:
                flash(e)
        elif request.form['submit_button'] == 'Recreate database':
            if not db.check_connection():
                flash('No database conncetion')
            else:
                try:
                    result = db.recreate_db()
                    flash(result)
                except Exception as e:
                    flash(e)

    return render_template(
        'health.html.j2',
        title = 'Health check',
        student = config.cfg['student'],
        hostname = aws.get_instance_hostname(),
        db_connection = db.check_connection().info,
        s3_connection = aws.check_s3_access()
    )

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html.j2'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html.j2'), 500
