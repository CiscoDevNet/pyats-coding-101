'''
Parsing JSON
------------

Python comes with a built-in module called 'json'. It contains the necessary
methods and functionality to parse & build JSON strings.

Read more at https://docs.python.org/3/library/json.html
'''

# the built-in module to handle json
import json

JSON_STRING = '''
{
    "string": "hello world",
    "boolean": true,
    "null": null,
    "numbers": 1234567,
    "object": {
        "key": "value",
        "another_key": "another_value"
    },
    "arrays": [
        "item_1",
        "item_2",
        "item_3"
    ]
}
'''

PYTHON_DICT = {
    'arrays': ['item_1', 'item_2', 'item_3'],
    'boolean': True,
    'null': None,
    'numbers': 1234567,
    'object': {'another_key': 'another_value', 'key': 'value'},
    'string': 'hello world'
}

# convert a json string to python object
converted_object = json.loads(JSON_STRING)

# the converted object is a dictionary
print(converted_object["string"])

# you can also convert structures back from python to json
converted_to_json = json.dumps(PYTHON_DICT)