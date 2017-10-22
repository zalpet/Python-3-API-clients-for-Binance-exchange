##The binance_api.py file contains the code for the Python language.
##It is intended for writing bots for trading on the Binance exchange.
##Examples of using commands are described in the same file and are commented out.


import hmac
import hashlib
import json
import time
import http.client
import copy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


server='www.binance.com'
# You must record your api key and secret key below:
api_key = 'your api key'
api_secret = 'your secret key'

recvWindow=60000
time_sleep=1.1 # Time interval, to delay requests to the exchange in sec

#####################  Public
def timestamp():
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='time'
        param=''
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: timestamp')
        return 'error'
    
def depth(symbol, limit=100):
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='depth'
        param='symbol='+symbol+'&limit='+str(limit)
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: depth')
        return 'error'
    

def aggTrades(symbol, startTime, endTime):
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='aggTrades'
        param='symbol='+symbol+'&startTime='+str(startTime)+'&endTime='+str(endTime)
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: aggTrades')
        return 'error'
    


def klines(symbol, interval, startTime, endTime):
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='klines'
        param='symbol='+symbol+'&interval='+str(interval)+'&startTime='+str(startTime)+'&endTime='+str(endTime)
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: klines')
        return 'error'



def hr24(symbol):
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='ticker/24hr'
        param='symbol='+symbol
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: hr24')
        return 'error'       


def allPrices():
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='ticker/allPrices'
        param=''
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: allPrices')
        return 'error'


def allBookTickers():
    time.sleep(time_sleep)
    try:
        api_path='/api/v1/'
        command='ticker/allBookTickers'
        param=''
        path=api_path+command+'?'+param  
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print ('Binance error in public request: allBookTickers')
        return 'error'



############################ Private    

def account():
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='account'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=''
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: account')
        return 'error'


def test_order (symbol, side,  quantity,  price):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='order/test'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=('symbol='+symbol+'&side='+side+'&type=LIMIT'+'&timeInForce=GTC'+
               '&quantity='+'{0:.8f}'.format(quantity)+'&price='+'{0:.8f}'.format(price))
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('POST', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('LBinance error in private request: order_book_all: test_order')
        return 'error'



def new_order_limit (symbol, side,  quantity,  price):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='order'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=('symbol='+symbol+'&side='+side+'&type=LIMIT'+'&timeInForce=GTC'+
               '&quantity='+'{0:.8f}'.format(quantity)+'&price='+'{0:.8f}'.format(price))
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('POST', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: order_book_all: new_order')
        return 'error'


def new_order_market (symbol, side,  quantity,  price):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='order'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=('symbol='+symbol+'&side='+side+'&type=MARKET'+'&timeInForce=GTC'+
               '&quantity='+'{0:.8f}'.format(quantity)+'&price='+'{0:.8f}'.format(price))
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('POST', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: order_book_all: new_order')
        return 'error'

def status_order (symbol, origClientOrderId):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='order'       
        time_data='&recvWindow='+str(recvWindow)+ '&origClientOrderId='+origClientOrderId+'&timestamp='+ timestamp
        param=('symbol='+symbol)
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: order_book_all: status_order')
        return 'error'

def cancel_order (symbol, clientOrderId):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='order'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=('symbol='+symbol+'&clientOrderId='+str('clientOrderId'))
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('DELETE', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: order_book_all: cancel_order')
        return 'error'


def open_orders (symbol):
    try:
        timestamp = str(int(time.time() * 1000))
        time.sleep(time_sleep)
        api_path='/api/v3/'
        command='openOrders'       
        time_data='&recvWindow='+str(recvWindow)+'&timestamp='+ timestamp
        param=('symbol='+symbol)
        data=param+time_data
        sign=hmac.new((api_secret).encode(), data.encode(), hashlib.sha256).hexdigest() 
        path=api_path+command+'?'+data+'&signature='+sign    
        headers={'X-MBX-APIKEY': api_key}
        conn = http.client.HTTPSConnection(server)
        conn.request('GET', path, '', headers) 
        response = conn.getresponse()
        data = json.load(response)
        conn.close()
        return data
    except:
        print('Binance error in private request: order_book_all: open_orders')
        return 'error'


def askbid(symbol):
    j=0
    while j<1e20:
        r = hr24(symbol)
        if (r=='error') :
            print('hr24, error, all_pairs=', r)
            time.sleep(time_sleep)
            j=j+1
        else:
            break
    return {'askPrice': float(r.get('askPrice')), 'bidPrice':  float(r.get('bidPrice'))}



# EXAMPLES:


#  - Getting latest price of a symbol    
# Example 1: askbid('BCCBTC')
# Output: {'askPrice': 0.056015, 'bidPrice': 0.055667} 


##- Getting depth of a symbol or maintain a depth cache locally
# Example 2: depth('ETHBTC', 10)
#Output:
##    {'lastUpdateId': 16180041, 'bids': [['0.05865100', '4.70200000', []], ['0.05865000', '0.96600000', []], ['0.05860700', '10.51800000', []],
##    ['0.05845200', '8.31000000', []], ['0.05845100', '9.10000000', []], ['0.05824200', '5.00000000', []], ['0.05824100', '16.04500000', []], [
##    '0.05824000', '51.55600000', []], ['0.05823900', '8.00100000', []], ['0.05823700', '8.80100000', []]], 'asks':
##    [['0.05869700', '1.74900000', []], ['0.05878400', '0.21000000', []], ['0.05878800', '0.90700000', []],
##    ['0.05887300', '0.00800000', []], ['0.05889300', '7.00000000', []], ['0.05908100', '1.77000000', []],
##    ['0.05908200', '10.00000000', []], ['0.05908900', '6.94000000', []], ['0.05909000', '2.53400000', []],
##    ['0.05910000', '11.60400000', []]]}



##- Placing a LIMIT order
# Example 3: new_order_limit('IOTABTC', 'BUY',  1000,  0.65)


##- Placing a MARKET order
# Example 3: new_order_market('IOTABTC', 'SELL',  1000,  0.65)


##- Checking an order’s status
# Example 4: status_order('NEOBTC','TEin9lrUrQdfjO5xRGEhlu')
#Output:
##'symbol': 'NEOBTC', 'orderId': 5831688, 'clientOrderId': 'TEin9lrUrQdfjO5xRGEhlu', 'price': '0.00456300', 'origQty': '0.49000000',
##'executedQty': '0.00000000', 'status': 'CANCELED','timeInForce': 'GTC',
##'type': 'LIMIT', 'side': 'BUY', 'stopPrice': '0.00000000', 'icebergQty': '0.00000000', 'time': 1508053486880}


##- Cancelling an order
# Exampe 5: cancel_order('NEOBTC','TEin9lrUrQdfjO5xRGEhlu')


##- Getting list of open orders
# Exampe 6: open_orders('NEOBTC')
# Output: 
##[{'symbol': 'NEOBTC', 'orderId': 5832074, 'clientOrderId': 'wnSP9BChRr44JvuHCBGtxN',
##'price': '0.00454700', 'origQty': '0.50000000', 'executedQty': '0.00000000',
##'status': 'NEW', 'timeInForce': 'GTC', 'type': 'LIMIT', 'side': 'BUY',
##'stopPrice': '0.00000000', 'icebergQty': '0.00000000', 'time': 1508053963009}]


##- Getting list of current position
#Example 7: account()


