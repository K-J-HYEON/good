# 문제1) 상승장? 하락장?

# 힌트
import requests
url = 'https://api.bithumb.com/public/ticker/btc'
data = { k: float(v) for k, v in requests.get(url).json()['data'].items() }

print("상승장") if (data['opening_price'] + (data['max_price']-data['min_price'])) > data['max_price'] else print('하락장')

# if (data['opening_price'] + (data['max_price']-data['min_price'])) > data['max_price']:

#     print("상승장")

# else:
#     print("하락장")



