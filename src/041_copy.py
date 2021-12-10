import pandas as pd
import urllib.parse
import json
import copy
import os
import hashlib
import datetime
import itertools

import shutil

dirMap = {
    "item" : "/Users/nakamurasatoru/git/d_omeka/omekac_dd/docs",
    "object" : "/Users/nakamurasatoru/git/d_omeka/omekac_dd2/docs",
}

for key in dirMap:

    dir1 = dirMap[key]
    dir2 = "/Users/nakamurasatoru/git/d_kunshujo/kunshujo-a/docs/{}".format(key)

    map = {
        dir1 + "/files/thumbnail" : dir2 + "/files/thumbnail",
        dir1 + "/pd" : dir2 + "/pd",
        dir1 + "/pp" : dir2 + "/pp"
    }

    for i in map:
        out = map[i]
        if os.path.exists(out):
            shutil.rmtree(out)
        shutil.copytree(i, out)