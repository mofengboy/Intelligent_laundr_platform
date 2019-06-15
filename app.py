from flask import Flask
import json
# 鉴权
from application.com.huawei.iotplatform.client.invokeapi.AuthenticationApi import AuthenticationApi

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 鉴权
@app.route('/auth')
def auth():
    authentication_api = AuthenticationApi()
    result = authentication_api.auth()
    return result


# 刷新token
@app.route('/refresh_auth')
def refresh_auth():
    authentication_api = AuthenticationApi()
    result = authentication_api.refresh_auth()
    return result


if __name__ == '__main__':
    app.run()
