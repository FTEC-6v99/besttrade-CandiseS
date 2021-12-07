import json
from flask import Blueprint
from app.src.db.dao import get_all_portfolios as dao
from app.src.domain.Portfolio import Portfolio


portfoliobp = Blueprint('portfolio', __name__, url_prefix="/portfolio")

@portfoliobp.route('/get-all-portfolios/', methods = ['GET'])
def get_all_portfolios() -> Portfolio:

    try:
        portfolio = get_all_portfolios
        if portfolio is None:
            return json.dumps([]), 200
        else:
            return json.dumps(portfolio.__dict__), 200
    except Exception as e:
        return 'Oops an error occured:' + str(e), 500