import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskDemo import app, db, bcrypt
from flaskDemo.forms import ProjectForm, ProjectUpdateForm, RegistrationForm, LoginForm, UpdateAccountForm, PostForm, DeptForm,DeptUpdateForm
from flaskDemo.models import User, Post, Item, Order, Order_Contents
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from sqlalchemy import exc


@app.route("/")
@app.route("/home")
def home():
    results = Order_Contents.query.all()
    return render_template('ordercontents_home.html', joined_m_n = results)
    posts = Post.query.all()
    return render_template('home.html', posts=posts)
    results2 = Item.query.join(Order_Contents,Item.item_id == Order_Contents.item_id) \
               .add_columns(Item.name, Order_Contents.item_id) \
               .join(Order, Order_Contents.order_id == Order.order_id).add_columns(Order_Contents.order_id)
    results = Faculty.query.join(Qualified,Faculty.facultyID == Qualified.facultyID) \
              .add_columns(Faculty.facultyID, Faculty.facultyName, Qualified.Datequalified, Qualified.courseID)
    return render_template('join.html', title='Join',joined_1_n=results, joined_m_n=results2)



@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@app.route("/dept/new", methods=['GET', 'POST'])
@login_required
def new_dept():
    form = DeptForm()
    if form.validate_on_submit():
        dept = Department(dname=form.dname.data, dnumber=form.dnumber.data,mgr_ssn=form.mgr_ssn.data,mgr_start=form.mgr_start.data)
        db.session.add(dept)
        db.session.commit()
        flash('You have added a new department!', 'success')
        return redirect(url_for('home'))
    return render_template('create_dept.html', title='New Department',
                           form=form, legend='New Department')


@app.route("/dept/<dnumber>")
@login_required
def dept(dnumber):
    dept = Department.query.get_or_404(dnumber)
    return render_template('dept.html', title=dept.dname, dept=dept, now=datetime.utcnow())


@app.route("/dept/<dnumber>/update", methods=['GET', 'POST'])
@login_required
def update_dept(dnumber):
    dept = Department.query.get_or_404(dnumber)
    currentDept = dept.dname

    form = DeptUpdateForm()
    if form.validate_on_submit():          # notice we are are not passing the dnumber from the form
        if currentDept !=form.dname.data:
            dept.dname=form.dname.data
        dept.mgr_ssn=form.mgr_ssn.data
        dept.mgr_start=form.mgr_start.data
        db.session.commit()
        flash('Your department has been updated!', 'success')
        return redirect(url_for('dept', dnumber=dnumber))
    elif request.method == 'GET':              # notice we are not passing the dnumber to the form

        form.dnumber.data = dept.dnumber
        form.dname.data = dept.dname
        form.mgr_ssn.data = dept.mgr_ssn
        form.mgr_start.data = dept.mgr_start
    return render_template('create_dept.html', title='Update Department',
                           form=form, legend='Update Department')


@app.route("/assignProj", methods=['GET', 'POST'])
@login_required
def assignProj():
    form = ProjectUpdateForm()
    
    if form.validate_on_submit():
        project = Order_Contents(order_id=form.orderid.data, item_id=form.itemid.data, quantity=1)
        db.session.add(project)
        try:
            db.session.commit()
            flash('You have added a new order!', 'success')
            return redirect(url_for('home'))
        except exc.IntegrityError as err:
            db.session.rollback()
            err_msg = err.args[0]
            if "Duplicate entry" in err_msg:
                flash("Duplicate order entry; (order has already been made)", "failed")
                return redirect(url_for("assignProj"))
    return render_template('assignProj.html', title='New Project',
                           form=form, legend='New Project')

@app.route("/dept/<dnumber>/delete", methods=['POST'])
@login_required
def delete_dept(dnumber):
    dept = Department.query.get_or_404(dnumber)
    db.session.delete(dept)
    db.session.commit()
    flash('The department has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/assign/<orderid>/<itemid>")
@login_required
def assign(orderid, itemid):
    assign = Order_Contents.query.get_or_404([orderid,itemid])
    return render_template('assign.html',title=str(assign.orderid)+"_"+str(assign.itemid),assign=assign,now=datetime.utcnow())

@app.route("/assign/<orderid>/<itemid>delete",methods=['POST'])
@login_required
def delete_assign(orderid,itemid):
    assign = Order_Contents.query.get_or_404([orderid,itemid])
    db.session.delete(assign)
    db.session.commit()
    flash('The project and essn with it has been deleted!', 'Success!')
    return redirect(url_for('home'))

@app.route("/assign/<orderid>/<itemid>/update",methods=['GET','POST'])
@login_required
def update_assign(orderid,itemid):
    flash('Update page under construction')
    return redirect(url_for('home'))
    
