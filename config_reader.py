"""Config file reader for master moudle"""
import configparser


def read(file="config.cfg"):
    config = configparser.ConfigParser()

    config.read(file)

    conf = {
        # SYSTEM
        # "screen_res": config["SYSTEM"]["screen_res"],
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

        # MUSIC
        "music_path": config["MUSIC"]["music_path"],
    }

    if conf["music_path"] == "none":
        conf["music_path"] = None

    if conf["pulsing"].lower() == "false":
        conf["pulsing"] = False
    elif conf["pulsing"].lower() == "true":
        conf["pulsing"] = True
    else:
        print("Error: unknow type")
        return

    # conf["screen_res"] = [int(n) for n in conf["screen_res"].split(', ')]

    return conf


if __name__ == "__main__":
    try:
        if read() is not None:
            print(read())
    except Exception as err:
        print(f"Error: {err}")
