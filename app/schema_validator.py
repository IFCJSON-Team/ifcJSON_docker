import json
import os
from jsonschema import validate, ValidationError, SchemaError


def json_validate(in_file_path, options={}):
    schema_file_path = "./IFC4.json"
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)
        filename = os.path.basename(in_file_path)
        with open(in_file_path, "r") as json_file:
            instance = json.load(json_file)
            try:
                validate(instance=instance, schema=schema)
                return f"{filename} is valid ifcJSON"
            except SchemaError as e:
                return "There is an error with the schema"
            except ValidationError as e:
                return f"{filename} is NOT valid ifcJSON! {e}, {e.message}"
                
# if __name__ == '__main__':
#     json_validate("./upload/basin-advanced-brep.json")