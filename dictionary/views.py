from flask import Flask, flash, request, render_template, url_for, abort
from flask_bootstrap import Bootstrap
from flask_login import login_user, login_required, logout_user
from werkzeug.utils import redirect

from forms import LoginForm
from models import User

app = Flask(__name__)
Bootstrap(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user_id = form.id.data
    if form.validate_on_submit():
        user = User.get_id(user_id)
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # if not is_safe_url(next):
        #     return abort(400)

        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
