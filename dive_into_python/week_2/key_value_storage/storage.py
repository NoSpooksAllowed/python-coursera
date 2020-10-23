import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="you have to enter a key name")
parser.add_argument("--val", help="you have to eneter a value name")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), "storage.data")
data = {}

if args.key and args.val:
    if not os.path.exists(storage_path):
        with open(storage_path, "w") as f:
            data = {
                args.key : [args.val],
            }
            json.dump(data, f)
    else:
        with open(storage_path, "r") as f:
            data = json.load(f)

        with open(storage_path, "w") as f:
            if args.key in data:
                data[args.key].append(args.val)
            else:
                data.setdefault(args.key, [args.val])
            json.dump(data, f)

elif args.key:
    if not os.path.exists(storage_path):
        print(None) 
    else:
        with open(storage_path, "r") as f:
            data = json.load(f)

            if args.key not in data:
                print(None)
            else:
                print(", ".join(map(str, data[args.key])))
else:
    print("usage storage.py --key [key_name] --val [value]")