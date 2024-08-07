from flask import Blueprint, render_template, send_file, redirect, url_for, request
from .pdf_generator import generate_pdf
from .models import User
from .database import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/generate-pdf')
def get_pdf():
    users = User.query.all()
    pdf_path = generate_pdf(users)
    return send_file(pdf_path, as_attachment=True, download_name='user_report.pdf')

@main.route('/add-user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.index'))