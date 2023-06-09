# NOTE: Generated By HttpRunner v4.3.0
# FROM: select_token.yml
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseSelectToken(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/cgi-bin/token")
            .get("https://api.weixin.qq.com/cgi-bin/token")
            .with_params(
                **{
                    "appid": "wxe6d35c5fb83d7039",
                    "grant_type": "client_credential",
                    "secret": "648f2af46d5cfd59fc0feb2b6c4019e0",
                }
            )
            .with_headers(
                **{
                    "Authorization": "Basic MTox",
                    "Postman-Token": "1d99e8cc-c73f-47a2-9620-4aed0320ea85",
                    "User-Agent": "PostmanRuntime/7.32.2",
                }
            )
            .extract()
            .with_jmespath("body.access_token", "access_token")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/cgi-bin/tags/get")
            .get("https://api.weixin.qq.com/cgi-bin/tags/get")
            .with_params(**{"access_token": "$access_token"})
            .with_headers(
                **{
                    "Postman-Token": "f7f5a6e0-f6b9-4bfb-8ef6-f0a2ef742286",
                    "User-Agent": "PostmanRuntime/7.32.2",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseSelectToken().test_start()
