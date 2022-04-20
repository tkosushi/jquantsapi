## jquantsapi
  
公式ドキュメント：https://jpx.gitbook.io/j-quants-api/  

### 必要なパッケージ
requestsをインストールしてください。  
  
```
pip install requests
```

### サンプル
  
```
import jquantsapi

token = 'YOUR TOKEN'
api = jquantsapi.API(token)

# 銘柄情報照会
response = api.get_listed_info()
# 日次の株価情報
response = api.get_daily_quotes('86970')
# 四半期の財務情報
response = api.get_fins_statements('86970')
# 翌日決算発表予定
response = api.get_fins_announcement()
```
  