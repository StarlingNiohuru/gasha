from flask import render_template, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from config import MAIN_LANGUAGE
from . import main


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated:
        return render_template('index.html', main_language=MAIN_LANGUAGE)
    else:
        return redirect(url_for('auth.login'))


@main.route('/self-self')
@login_required
def self_self():
    return render_template('self-self.html', main_language=MAIN_LANGUAGE)


@main.route('/self-english')
@login_required
def self_english():
    return render_template('self-eng.html', main_language=MAIN_LANGUAGE)


@main.route('/self-chinese')
@login_required
def self_chinese():
    return render_template('self-zho.html', main_language=MAIN_LANGUAGE)


@main.route('/self-japanese')
@login_required
def self_japanese():
    return render_template('self-jpn.html', main_language=MAIN_LANGUAGE)
