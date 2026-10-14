import ccxt
import pandas as pd
import time
from datetime import datetime

print("=== SIMPLE TRADING BOT STARTED ===")

# Setup exchange (public data, no API key needed for price check)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1m'

print(f"Fetching {symbol} candles...")

def get_signal():
    try:
        # Get last 50 candles
        candles = exchange.fetch_ohlcv(symbol, timeframe, limit=50)
        df = pd.DataFrame(candles, columns=['time','open','high','low','close','vol'])
        # Simple moving averages
        df['sma_fast'] = df['close'].rolling(10).mean()
        df['sma_slow'] = df['close'].rolling(30).mean()
        
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last['close']
        print(f"[{datetime.now()}] Price: {price:.2f} | SMA10: {last['sma_fast']:.2f} | SMA30: {last['sma_slow']:.2f}")
        
        # Buy signal: fast crosses above slow
        if prev['sma_fast'] < prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
            return "BUY SIGNAL"
        elif prev['sma_fast'] > prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
            return "SELL SIGNAL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error: {e}")
        return "ERROR"

# Loop
while True:
    signal = get_signal()
    print(f"--> Decision: {signal}\n")
    time.sleep(10)
cat > bot.py << 'PYEOF'
import ccxt
import pandas as pd
import time
from datetime import datetime

print("=== SIMPLE TRADING BOT STARTED ===")

# Setup exchange (public data, no API key needed for price check)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1m'

print(f"Fetching {symbol} candles...")

def get_signal():
    try:
        # Get last 50 candles
        candles = exchange.fetch_ohlcv(symbol, timeframe, limit=50)
        df = pd.DataFrame(candles, columns=['time','open','high','low','close','vol'])
        # Simple moving averages
        df['sma_fast'] = df['close'].rolling(10).mean()
        df['sma_slow'] = df['close'].rolling(30).mean()
        
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last['close']
        print(f"[{datetime.now()}] Price: {price:.2f} | SMA10: {last['sma_fast']:.2f} | SMA30: {last['sma_slow']:.2f}")
        
        # Buy signal: fast crosses above slow
        if prev['sma_fast'] < prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
            return "BUY SIGNAL"
        elif prev['sma_fast'] > prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
            return "SELL SIGNAL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error: {e}")
        return "ERROR"

# Loop
while True:
    signal = get_signal()
    print(f"--> Decision: {signal}\n")
    time.sleep(10)
cat > bot.py << 'PYEOF'
import ccxt
import pandas as pd
import time
from datetime import datetime

print("=== SIMPLE TRADING BOT STARTED ===")

# Setup exchange (public data, no API key needed for price check)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1m'

print(f"Fetching {symbol} candles...")

def get_signal():
    try:
        # Get last 50 candles
        candles = exchange.fetch_ohlcv(symbol, timeframe, limit=50)
        df = pd.DataFrame(candles, columns=['time','open','high','low','close','vol'])
        # Simple moving averages
        df['sma_fast'] = df['close'].rolling(10).mean()
        df['sma_slow'] = df['close'].rolling(30).mean()
        
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last['close']
        print(f"[{datetime.now()}] Price: {price:.2f} | SMA10: {last['sma_fast']:.2f} | SMA30: {last['sma_slow']:.2f}")
        
        # Buy signal: fast crosses above slow
        if prev['sma_fast'] < prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
            return "BUY SIGNAL"
        elif prev['sma_fast'] > prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
            return "SELL SIGNAL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error: {e}")
        return "ERROR"

# Loop
while True:
    signal = get_signal()
    print(f"--> Decision: {signal}\n")
    time.sleep(10)
cat > bot.py << 'PYEOF'
import ccxt
import pandas as pd
import time
from datetime import datetime

print("=== SIMPLE TRADING BOT STARTED ===")

# Setup exchange (public data, no API key needed for price check)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1m'

print(f"Fetching {symbol} candles...")

def get_signal():
    try:
        # Get last 50 candles
        candles = exchange.fetch_ohlcv(symbol, timeframe, limit=50)
        df = pd.DataFrame(candles, columns=['time','open','high','low','close','vol'])
        # Simple moving averages
        df['sma_fast'] = df['close'].rolling(10).mean()
        df['sma_slow'] = df['close'].rolling(30).mean()
        
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last['close']
        print(f"[{datetime.now()}] Price: {price:.2f} | SMA10: {last['sma_fast']:.2f} | SMA30: {last['sma_slow']:.2f}")
        
        # Buy signal: fast crosses above slow
        if prev['sma_fast'] < prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
            return "BUY SIGNAL"
        elif prev['sma_fast'] > prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
            return "SELL SIGNAL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error: {e}")
        return "ERROR"

# Loop
while True:
    signal = get_signal()
    print(f"--> Decision: {signal}\n")
    time.sleep(10)
cat > bot.py << 'PYEOF'
import ccxt
import pandas as pd
import time
from datetime import datetime

print("=== SIMPLE TRADING BOT STARTED ===")

# Setup exchange (public data, no API key needed for price check)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

symbol = 'BTC/USDT'
timeframe = '1m'

print(f"Fetching {symbol} candles...")

def get_signal():
    try:
        # Get last 50 candles
        candles = exchange.fetch_ohlcv(symbol, timeframe, limit=50)
        df = pd.DataFrame(candles, columns=['time','open','high','low','close','vol'])
        # Simple moving averages
        df['sma_fast'] = df['close'].rolling(10).mean()
        df['sma_slow'] = df['close'].rolling(30).mean()
        
        last = df.iloc[-1]
        prev = df.iloc[-2]
        
        price = last['close']
        print(f"[{datetime.now()}] Price: {price:.2f} | SMA10: {last['sma_fast']:.2f} | SMA30: {last['sma_slow']:.2f}")
        
        # Buy signal: fast crosses above slow
        if prev['sma_fast'] < prev['sma_slow'] and last['sma_fast'] > last['sma_slow']:
            return "BUY SIGNAL"
        elif prev['sma_fast'] > prev['sma_slow'] and last['sma_fast'] < last['sma_slow']:
            return "SELL SIGNAL"
        else:
            return "HOLD"
    except Exception as e:
        print(f"Error: {e}")
        return "ERROR"

# Loop
while True:
    signal = get_signal()
    print(f"--> Decision: {signal}\n")
    time.sleep(10)

pyeof
pyeof
