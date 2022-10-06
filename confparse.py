"""Config file reader"""
import configparser
import logging
import sys

def read(file="config.cfg", path=None):
    if path:
        if path[-1] == '/':
            file = f"{path}{file}"
        else:
            file = f"{path}/{file}"

    config = configparser.ConfigParser()

    config.read(f"{file}")

    conf = {
        # SYSTEM
        "radius": int(config["SYSTEM"]["radius"]),
        "num_lines": int(config["SYSTEM"]["num_lines"]),
        "anim_speed": float(config["SYSTEM"]["anim_speed"]),
        "fps": int(config["SYSTEM"]["fps"]),
        "pulsing": config["SYSTEM"]["pulsing"],

        # COLORS
        "color_mode": config["COLORS"]["color_mode"],
        "bg_color": config["COLORS"]["bg_color"],
        "mono_color": config["COLORS"]["mono_color"],
        "multi_color_1": config["COLORS"]["multi_color_1"],
        "multi_color_2": config["COLORS"]["multi_color_2"],
    }

    if conf["pulsing"].lower() == "false":
        conf["pulsing"] = False
    elif conf["pulsing"].lower() == "true":
        conf["pulsing"] = True
    else:
        logging.fatal("error: unknow type  -  file: config_reader.py")
        return None

    return conf


if __name__ == "__main__":
    logging.basicConfig(
        filename='main.log',
        filemode='a',
        format='%(asctime)s - %(name)s - [  %(levelname)s  ] - %(message)s'
    )

    if "--help" in sys.argv:
        print("this moudle reading config file and outputting in python dict format")
        sys.exit(0)

    try:
        parsed_config = read()

        if parsed_config is not None:
            print(parsed_config)

    except Exception as err:
        logging.fatal("error: %s  -  file:config_reader.py", err)
