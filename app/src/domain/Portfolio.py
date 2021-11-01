class Portfolio():
    # create a class that mimics the database table: portfolio
    def __init__(self, portfolio_id: int, account_id: int, ticker: str, quantity: int, purchase_price: float) -> None:
        self.portfolio_id = portfolio_id
        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity
        self.purchase_price = purchase_price