from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import File
from app.files.forms import UploadForm
import os
from app import create_app

files = Blueprint('files', __name__)

@files.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = file.filename
        file_path = os.path.join(create_app().config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        new_file = File(filename=filename, user_id=current_user.id)
        db.session.add(new_file)
        db.session.commit()
        flash('File successfully uploaded', 'success')
        return redirect(url_for('main.home'))
    return render_template('upload.html', form=form)
