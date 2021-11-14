# imports
from zipline.api import order_percent, symbol, record
from zipline.finance import commission

# parameters
SELECTED_STOCK = 'GS'

def initialize(context):
    context.asset = symbol(SELECTED_STOCK)
    context.has_ordered = False  
    context.set_commission(commission.PerShare(cost=0.0, min_trade_cost=0))

def handle_data(context, data):
    
    # trading logic
    if not context.has_ordered:
        order_percent(context.asset, 1)
        context.has_ordered = True
        
    record(price=data.current(context.asset, 'price'))