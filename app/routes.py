from flask import render_template, Blueprint

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=('GET', ))
def index():
    return render_template('home/index.html')
