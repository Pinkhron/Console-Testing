from datetime import datetime
import json

class tcolors:
    INFO = '\033[96m' # CYAN
    SUCCESS = '\033[92m' # GREEN
    WARNING = '\033[93m' # YELLOW
    ERROR = '\033[91m' # RED
    RESET = '\033[0m' # RESET COLOR

while True:

    # Time
    time = datetime.now()
    ftime = time.strftime("%m/%d/%Y %H:%M:%S")

    cfg_file = open("config.json")
    cfg = json.load(cfg_file)

    # Token Authenticator

    if cfg["token"] == "123":
        print(ftime + f"{tcolors.SUCCESS} SUCCESS {tcolors.RESET}" + "Token authenticated successfully.")
    else:
        print(ftime + f"{tcolors.ERROR} ERROR {tcolors.RESET}" + "Token is invalid.")
    break

# DATE TIME STATUS TEXT