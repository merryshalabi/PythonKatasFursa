import unittest
from katas.nginx_log_parser import parse_log  # Replace `your_module` with actual module name
from typing import Dict

class TestParseLog(unittest.TestCase):

    def test_valid_log(self):
        log = (
            '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] '
            '"GET /web-enabled/Enhanced-portal/bifurcated-forecast.js HTTP/1.1" 200 1684 '
            '"-" "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"'
        )
        expected: Dict[str, str] = {
            "client_ip": "122.176.223.47",
            "date": "05/Feb/2024:08:29:40 +0000",
            "http_method": "GET",
            "path": "/web-enabled/Enhanced-portal/bifurcated-forecast.js",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "1684",
            "user_agent": "Opera/9.58 (X11; Linux i686; en-US) Presto/2.12.344 Version/13.00"
        }

        self.assertEqual(parse_log(log), expected)

    def test_invalid_log_missing_fields(self):
        log = 'invalid log line'
        with self.assertRaises(ValueError):
            parse_log(log)

    def test_invalid_log_wrong_format(self):
        log = (
            '122.176.223.47 - - 05/Feb/2024:08:29:40 +0000 '
            '"GET /some/path HTTP/1.1" 200 1684 "-" "UserAgent/1.0"'
        )  # missing brackets
        with self.assertRaises(ValueError):
            parse_log(log)


if __name__ == "__main__":
    unittest.main()
