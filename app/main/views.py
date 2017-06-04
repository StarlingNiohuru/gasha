from flask import render_template, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from . import main


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated():
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))
