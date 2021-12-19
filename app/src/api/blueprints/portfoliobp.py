import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Portfolio import Portfolio


portfoliobp = bp = Blueprint('portfolio', __name__, url_prefix="/portfolio")

@bp.route('/get-all-portfolios', methods = ['GET'])
def get_all_portfolios() -> Portfolio:

    portfolios: t.list[Portfolio] = dao.get_all_portfolios()
    if len(portfolios) == 0:
        return json.dumps([])
    else:
        return json.dumps([portfolio.__dict__ for portfolio in portfolios])


    # try:
    #     portfolio = get_all_portfolios
    #     if portfolio is None:
    #         return json.dumps([]), 200
    #     else:
    #         return json.dumps(portfolio.__dict__), 200
    # except Exception as e:
    #     return 'Oops an error occured:' + str(e), 500