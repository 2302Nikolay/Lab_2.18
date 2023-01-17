import os

print("The keys and values of all environment variables:")
for key in os.environ:
    print(key, "=>", os.environ[key])

print("The value of HOME is: ", os.environ["HOME"])
