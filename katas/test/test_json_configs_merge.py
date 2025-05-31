import unittest
import tempfile
import json
import os
from katas.json_config_merge import json_configs_merge  # adjust import if needed

class TestJsonConfigsMerge(unittest.TestCase):

    def write_temp_json(self, content: dict) -> str:
        fd, path = tempfile.mkstemp(suffix=".json")
        with os.fdopen(fd, 'w') as f:
            json.dump(content, f)
        return path

    def test_merge_simple(self):
        file1 = self.write_temp_json({
            "user": {
                "name": "John",
                "age": 30
            },
            "settings": {
                "theme": "light"
            }
        })

        file2 = self.write_temp_json({
            "user": {
                "age": 31,
                "email": "john@example.com"
            },
            "settings": {
                "language": "spanish"
            }
        })

        expected = {
            "user": {
                "name": "John",
                "age": 31,
                "email": "john@example.com"
            },
            "settings": {
                "theme": "light",
                "language": "spanish"
            }
        }

        result = json_configs_merge(file1, file2)
        self.assertEqual(result, expected)

        # Cleanup
        os.remove(file1)
        os.remove(file2)

    def test_deep_merge(self):
        file1 = self.write_temp_json({
            "a": {
                "b": {
                    "c": 1
                }
            }
        })

        file2 = self.write_temp_json({
            "a": {
                "b": {
                    "d": 2
                }
            }
        })

        expected = {
            "a": {
                "b": {
                    "c": 1,
                    "d": 2
                }
            }
        }

        result = json_configs_merge(file1, file2)
        self.assertEqual(result, expected)

        os.remove(file1)
        os.remove(file2)

    def test_override_non_dict(self):
        file1 = self.write_temp_json({
            "a": 1
        })
        file2 = self.write_temp_json({
            "a": {
                "nested": True
            }
        })

        expected = {
            "a": {
                "nested": True
            }
        }

        result = json_configs_merge(file1, file2)
        self.assertEqual(result, expected)

        os.remove(file1)
        os.remove(file2)

    def test_empty_input(self):
        result = json_configs_merge()
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()
