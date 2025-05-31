import json
from typing import Any


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    """
    Merge multiple JSON configuration files into a single dictionary.

    You are given an unknown number of file paths pointing to JSON configuration files.
    These files should be merged in the order they are given:
    - Keys in later files override those in earlier ones.
    - Nested dictionaries must also be merged recursively.

    Example:

        File: default.json
        {
          "user": {
            "name": "John",
            "age": 30
          },
          "settings": {
            "theme": "light",
            "language": "english"
          }
        }

        File: local.json
        {
          "user": {
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

        Result:
        {
          "user": {
            "name": "John",
            "age": 31,
            "email": "john@example.com"
          },
          "settings": {
            "theme": "light",
            "language": "spanish",
            "timezone": "UTC+1"
          }
        }

    Args:
        *json_paths: Variable number of JSON file paths to merge.

    Returns:
        dict: The merged configuration dictionary.
    """

    json_dictionary = {}
    for path in json_paths:
        with open(path,'r') as file:
            config = json.load(file)
            for key,val in config.items():
                if key in json_dictionary and isinstance(json_dictionary[key],dict) and isinstance(val,dict):
                    json_dictionary[key] = merge_json(json_dictionary[key],val)
                else :
                    json_dictionary[key] = val



    return json_dictionary

def merge_json(base,new):
    for key, value in new.items():
        if key in base and isinstance(base[key],dict) and isinstance(value,dict):
            base[key] = merge_json(base[key],value)
        else:
            base[key] = value
    return base



if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('default.json', 'production.json', 'us-east-1-production.json')
    print(config)
