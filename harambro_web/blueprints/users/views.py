from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from models.user import User

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    name = name.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)

    newuser = User(
        name=name,
        email=email,
        password=hashed_password
    )

    if newuser.save():
        flash('Welcome to Harambro.')
        return redirect(url_for('users.new'))

    else:
        flash(f'{user_email} is already taken. Please try again.')
        return render_template('new.html', errors=newuser.errors)