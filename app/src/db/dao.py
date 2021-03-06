# Database Access Object: file to interface with the database
# CRUD operations:
# C: Create
# R: Read
# U: Update
# D: Delete
import typing as t
from mysql.connector import connect, cursor
from mysql.connector.connection import MySQLConnection
import config
from app.src.domain.Investor import Investor
from app.src.domain.Account import Account
from app.src.domain.Portfolio import Portfolio

def get_cnx() -> MySQLConnection:
    return connect(**config.dbparams)

'''
    Investor DAO functions
'''

def get_all_investor() -> list[Investor]:
    '''
        Get list of all investors [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor'
    cursor.execute(sql)
    results: list[dict] = cursor.fetchall()
    for row in results:
        investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors

def get_investor_by_id(id: int) -> t.Optional[Investor]:
    '''
        Returns an investor object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where id = %s'
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    investor = Investor(row['name'], row['status'], row['id'])
    return investor 

def get_investors_by_name(name: str) -> list[Investor]:
    '''
        Return a list of investors for a given name [R]
    '''
    investors: list[Investor] = []
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from investor where name = %s'
    cursor.execute(sql, (name,))
    if cursor.rowcount == 0:
        investors = []
    else:
        rows = cursor.fetchall()
        for row in rows:
            investors.append(Investor(row['name'], row['status'], row['id']))
    db_cnx.close()
    return investors


def create_investor(investor: Investor) -> None:
    '''
        Create a new investor in the db given an investor object [C]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into investor (name, status) values (%s, %s)'
    cursor.execute(sql, (investor.name, investor.status))
    db_cnx.commit()
    db_cnx.close()

def delete_investor(id: int):
    '''
        Delete an investor given an id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from investor where id = %s'
    cursor.execute(sql, (id,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()

def update_investor_name(id: int, name: str) -> None:
    '''
        Updates the investor name [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set name = %s where id = %s'
    cursor.execute(sql, (id, name))
    db_cnx.commit()
    db_cnx.close()

def update_investor_status(id: int, status: str) -> None:
    '''
        Update the inestor status [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update investor set status = %s where id = %s'
    cursor.execute(sql, (id, status))
    db_cnx.commit()
    db_cnx.close()

'''
    Account DAO functions
'''
def get_all_accounts() -> list[Account]:
    '''
    Returns an Account object given an account_number [R]
'''
    accounts: list[Account] = []
    db_cnx: MySQLConnection = get_cnx()
    cur = db_cnx.cursor(dictionary=True)
    sql: str = 'select * from account;'
    cur.execute(sql)

    results: list[dict] = cur.fetchall()
    for row in results:
        accounts.append(Account(row['account_number'], row['balance'], row['investor_id']))
    db_cnx.close()
    return accounts

###########

              

def get_account_by_id(id: int) -> Account:
    '''
    Returns a list of account_numbers [R]
'''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        account = Account(row['account_number'], row['investor_id'], row['balance'])
        return account     

def get_accounts_by_investor_id(investor_id: int) ->  list[Account]:

    '''
        Returns an account object given an investor ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    sql: str = 'select * from account where investor_id = %s'
    cursor.execute(sql, (investor_id,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        account = Account(row['account_number'], row['investor_id'], row['balance'])
        return account 








def delete_account(account_number: int) -> None:
    '''
        Delete an account given an account_number [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from account where account_number = %s'
    cursor.execute(sql, (account_number,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()
    

def update_acct_balance(account_number: int, balance: float) -> None:
    '''
        Updates the account balance [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'update account set balance = %s where account_number = %s'
    cursor.execute(sql, (account_number, balance))
    db_cnx.commit()
    db_cnx.close()
    

def create_account(account: Account) -> None:
    '''
    Create a new account in the db given an account object [C]
'''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (investor_id, balance) values (%s, %s)'
    cursor.execute(sql, (account.investor_id, account.balance))
    db_cnx.commit()
    db_cnx.close()

'''
    Portfolio DAO functions
'''
def get_all_portfolios() -> list[Portfolio]:
    '''
        Get list of all portfolios [R]
    '''

    
    portfolios: list[Portfolio] = []
    db_cnx: MySQLConnection = get_cnx()
    cur = db_cnx.cursor(dictionary=True)
    sql: str = 'select * from portfolio;'
    cur.execute(sql)

    results: list[dict] = cur.fetchall()
    for row in results:
        portfolios.append(Portfolio(row['portfolio_id'], row['account_number'], row['ticker'], row['quantity'], row['purchase_price']))
    db_cnx.close()
    return portfolios


    # portfolios: list[Portfolio] = []
    # db_cnx: MySQLConnection = get_cnx()
    # cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = True
    # sql: str = 'select * from portfolio'
    # cursor.execute(sql)
    # results: list[dict] = cursor.fetchall()
    # for row in results:
    #     portfolios.append(Portfolio(row['portfolio_id'], row['account_number'], row['ticker'], row['quantity'], row['purchase_price']))
    # db_cnx.close()
    # return portfolios
    

def get_porfolios_by_acct_id(account_number: int) -> list[Portfolio]:
    '''
        Returns an account_number object given an account_number [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = Tru
    sql: str = 'select * from portfolio where account_number = %s'
    cursor.execute(sql, (account_number,))
    if cursor.rowcount == 0:
        return None
    else:
        row = cursor.fetchone()
        portfolio = Portfolio(row['portfolio_id'], row['account_number'], row['ticker'], row['quantity'], row['purchase_price'])
        db_cnx.close()
        return portfolio
        
 
    

def get_portfolios_by_portfolio_id(portfolio_id: int) -> list[Portfolio]:
    '''
        Returns an portfolio_id object given an account_number ID [R]
    '''
    db_cnx: MySQLConnection = get_cnx()
    cursor = db_cnx.cursor(dictionary=True) # always pass dictionary = Tru
    sql: str = 'select * from portfolio where portfolio_id = %s'
    cursor.execute(sql, (portfolio_id,))
    if cursor.rowcount == 0:
        db_cnx.close()
        return None
    else:
        row = cursor.fetchone()
        portfolio = Portfolio(row['portfolio_id'], row['account_number'], row['ticker'], row['quantity'], row['purchase_price'])
        return portfolio
        db_cnx.close()
 
    


def delete_portfolio(portfolio_id: int) -> None:
    '''
        Delete an portfolio given an portfolio_id [D]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'delete from portfolio where portfolio_id = %s'
    cursor.execute(sql, (portfolio_id,))
    db_cnx.commit() # inserts, updates, and deletes
    db_cnx.close()
    

def buy_stock(ticker: str, price: float, quantity: int) -> None:
    '''
    Create/Buy Stock in the db given an account_number object [C]
'''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql = 'insert into account (ticker, purchase_price, quantity) values (%s, %s)'
    cursor.execute(sql, (ticker, purchase_price, quantity ))
    db_cnx.commit()
    db_cnx.close()


def sell_stock(ticket: str, quantity: int, sale_price: float) -> None:
    '''
        Updates the quantity and account balance (sell stock) [U]
    '''
    db_cnx = get_cnx()
    cursor = db_cnx.cursor()
    sql2 = 'select account_number, ticker, account.balance, (quantity - (Select(quantity from portfoilo)) as cur_quantity from portfolio where account_number = %s  and ticker = %s'
    sql = 'update portfolio set quantity = cur_quantity where account_number = %s'
    aql3 = 'update account set balance = new_balance where account_number = %s' 
    cursor.execute(sql, (account_number, ticker, quantity, account.balance))
    db_cnx.commit()
    db_cnx.close()   

    # 1. update quantity in portfolio table
    # 2. update the account balance:
    # Example: 10 APPL shares at $1/share with account balance $100
    # event: sale of 2 shares for $2/share
    # output: 8 APPLE shares at $1/share with account balance = 100 + 2 * (12 - 10) = $104
    
