import json

class tcolors:
    INFO = '\033[32m' # GREEN
    WARNING = '\033[33m' # YELLOW
    ERROR = '\033[31m' # RED
    RESET = '\033[0m' # RESET COLOR


def print_ln():
    print("Test123")


while True:
    print_ln()
    cfg_file = open("config.json")
    cfg = json.load(cfg_file)

    print("TOKEN: " + cfg["token"])
    print("")
    break

# DATE TIME STATUS TEXT