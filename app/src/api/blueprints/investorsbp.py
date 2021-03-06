import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Investor import Investor


investorbp = Blueprint('investor', __name__, url_prefix='/investor')

@investorbp.route('/get-investor-by-id/<id>', methods = ['GET'])
def get_investor_by_id(id: int)-> Investor:
    try:
        investor = dao.get_investor_by_id(id)
        if investor is None:
            return json.dumps([]), 200
        else:
            return json.dumps(investor.__dict__), 200
    except Exception as e:
        return 'Oops an error occured:' + str(e), 500
@investorbp.route('/get-all-investors', methods=['GET'])
def get_all_investors():

    investors: t.list[Investor] = dao.get_all_accounts()
    if len(investors) == 0:
        return json.dumps([])
    else:
        return json.dumps([investor.__dict__() for investor in investors])






    # try:
    #     investors = dao.get_all_investor()
    #     return json.dumps(investor.__dict__ for investor in investors)
    # except Exception as e:
    #     return 'Oops an error occured: ' + str(e), 500

