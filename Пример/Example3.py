import os

os.environ.setdefault("DEBUG", "True")

if os.environ.get("DEBUG") == "True":
    print("Debug mode is on")
else:
    print("Debug mode is off")
