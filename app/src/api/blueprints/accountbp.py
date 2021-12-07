
import json
from flask import Blueprint
import app.src.db.dao as dao
from app.src.domain.Account import Account


accountbp = Blueprint('account', __name__, url_prefix="/account")

@accountbp.route('/get-all-accounts', methods = ['GET'])
def get_all_accounts() -> Account:

    accounts: t.list[Account] = dao.get_all_accounts()
    if len(accounts) == 0:
        return json.dumps([])
    else:
        return json.dumps(accounts, default = lambda x: x.__dict__)
    ####
    try:
	    account = dao.get_all_accounts(account_number)
	    return json.dumps(account.__dict__)
    except Exception as e:
        return 500, "OOps there was a mistake!"
    #try:
	#    account = dao.get_all_accounts()
    #return json.dumps([]), 200
    
    #except Exception as e:
     #   return 'Oops an error occured:' + str(e), 500
