from flask import Blueprint, render_template
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio
from app.src.domain.Investor import Investor
import app.src.db.dao as dao

uibp = Blueprint('ui', __name__, url_prefix='/ui')

@uibp.route('/', methods = ['GET'])
def main():
    return render_template('home.html')

@uibp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@uibp.route('/investors', methods = ['GET'])
def investor():
    investors = dao.get_all_investor()
    return render_template('investors.html', investors = investors)

@uibp.route('/accounts',methods = ['GET'])
def account():
    accounts = dao.get_all_accounts()
    return render_template('accounts.html',accounts = accounts)

@uibp.route('/portfolios',methods = ['GET'])
def portfolio():
    portfolios = dao.get_all_portfolios()
    return render_template('portfolios.html',portfolios = portfolios)