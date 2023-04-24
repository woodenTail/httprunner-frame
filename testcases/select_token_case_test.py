# NOTE: Generated By HttpRunner v4.3.0
# FROM: testcases\select_token_case.yml
from httprunner import HttpRunner, Config, Step, RunRequest
from httprunner import RunTestCase

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from api.get_token_test import TestCaseGetToken as GetToken
from api.select_token_test import TestCaseSelectToken as SelectToken


class TestCaseSelectTokenCase(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(RunTestCase("/cgi-bin/token").call(GetToken).export(*["access_token"])),
        Step(RunTestCase("/cgi-bin/tags/get").call(SelectToken)),
    ]


if __name__ == "__main__":
    TestCaseSelectTokenCase().test_start()
