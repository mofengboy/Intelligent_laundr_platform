import json

from OceanConnect_Python_SDK.com.huawei.iotplatform.client.invokeapi.Authentication import Authentication

from application.com.huawei.iotplatform.client.dto.AuthOutDTO import AuthOutDTO
from application.com.huawei.iotplatform.client.dto.AuthRefreshInDTO import AuthRefreshInDTO
from application.com.huawei.iotplatform.constant.Constant import Constant
from application.com.huawei.iotplatform.client.invokeapiTest import AuthenticationTest


class AuthenticationApi:

    # 鉴权
    def auth(self):
        auTest = AuthenticationTest.AuthenticationTest()
        authentication = Authentication()

        ag = authentication.getAuthToken(Constant().clientInfo())

        # print("====== get access token ======")
        # print("result:", ag + "\n")
        return ag
        # ar = authentication.refreshAuthToken(auTest.refreshAuthTokenInfo())
        # print("====== refresh token ======")
        # print("result:", ar + "\n")
        # 刷先Token

    def refresh_auth(self):
        auTest = AuthenticationTest.AuthenticationTest()
        authentication = Authentication()

        # ag = authentication.getAuthToken(Constant().clientInfo())

        # print("====== get access token ======")
        # print("result:", ag + "\n")
        ar = authentication.refreshAuthToken(auTest.refreshAuthTokenInfo())
        # print("====== refresh token ======")
        # print("result:", ar + "\n")
        return ar

    def auth_test(self):
        return 'test auth'


if __name__ == '__main__':
    test = AuthenticationApi()
    test.auth()
