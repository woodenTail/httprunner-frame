# NOTE: Generated By HttpRunner v4.3.0
# FROM: sale_order_list.json
from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseSaleOrderList(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/prod-api/order/salesOrder/list")
            .get("http://192.168.200.135/prod-api/order/salesOrder/list")
            .with_params(
                **{
                    "pageNum": "1",
                    "pageSize": "10",
                    "status": "0",
                    "allProductData": "",
                }
            )
            .with_headers(
                **{
                    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjU0NDRjY2UxLWYwYmItNGRmNy04Yjc5LTczNDQ1NmZlZWYyMyJ9.QM2RahHLVXaesXEFio37p69WKvcj1zn8qRB_4uiUo3xGenAiJ55k_xz-rw1f_UoVVQwqZEs0VBKdSFlCdYNzqw",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
            .assert_equal("body.total", 1510)
            .assert_equal("body.code", 200)
            .assert_equal("body.msg", "查询成功")
        ),
    ]


if __name__ == "__main__":
    TestCaseSaleOrderList().test_start()