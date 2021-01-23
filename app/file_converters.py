import json
import os

import ifcjson


def ifc2json(in_file_path, options={}):

    if "compact" in options and options["compact"]:
        indent = None
        COMPACT = True
    else:
        indent = 2
        COMPACT = False

    if "no_inverse" in options and options["no_inverse"]:
        NO_INVERSE = True
    else:
        NO_INVERSE = False

    if "empty_properties" in options and options["empty_properties"]:
        EMPTY_PROPERTIES = True
    else:
        EMPTY_PROPERTIES = False

    if "no_ownerhistory" in options and options["no_ownerhistory"]:
        NO_OWNERHISTORY = True
    else:
        NO_OWNERHISTORY = False

    if "geometry" in options:
        if options["geometry"] == "none":
            GEOMETRY = False
        elif options["geometry"] == "tessellate":
            GEOMETRY = "tessellate"
        else:
            GEOMETRY = True
    else:
        GEOMETRY = True

    if "version" not in options or options["version"] == "4":
        return ifcjson.IFC2JSON4(in_file_path,
                                    COMPACT,
                                    NO_INVERSE=NO_INVERSE,
                                    EMPTY_PROPERTIES=EMPTY_PROPERTIES,
                                    NO_OWNERHISTORY=NO_OWNERHISTORY,
                                    GEOMETRY=GEOMETRY
                                    ).spf2Json()
    elif options["version"] == "5a":
        return ifcjson.IFC2JSON5a(in_file_path,
                                    COMPACT,
                                    EMPTY_PROPERTIES=EMPTY_PROPERTIES
                                    ).spf2Json()
    else:
        raise ValueError(
            'Version ' + options["version"] + ' is not supported')

def json2ifc(in_file_path, options={}):
    out_file_path = os.path.splitext(in_file_path)[0] + '.ifc'
    ifc_json = ifcjson.JSON2IFC(in_file_path)
    ifc_model = ifc_json.ifcModel()
    ifc_model.write(out_file_path)
    return out_file_path