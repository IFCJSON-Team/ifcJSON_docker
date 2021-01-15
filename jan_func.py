# IFCJSON_python - ifc2json.py
# Convert IFC SPF file to IFC.JSON
# https://github.com/IFCJSON-Team

# MIT License

# Copyright (c) 2020 Jan Brouwer <jan@brewsky.nl>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import ifcjson

def generate_json(ifcFilePath, jsonFilePath):
    COMPACT=False
    INCLUDE_INVERSE=False
    EMPTY_PROPERTIES=False
    NO_OWNERHISTORY=True
    GEOMETRY=True
    jsonData = ifcjson.IFC2JSON4(ifcFilePath, COMPACT, INCLUDE_INVERSE, EMPTY_PROPERTIES, NO_OWNERHISTORY, GEOMETRY).spf2Json()
    with open(jsonFilePath, 'w') as outfile:
        json.dump(jsonData, outfile, indent=True)
    return jsonData

# generate_json("model.ifc", "output.json")