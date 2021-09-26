def get_preferences(centre):
    time_prefs = {
        "A": lambda t: (abs(1 - t[0]), abs(2 - t[1])),
        "B": lambda t: (abs(centre[0] - t[0])),
        "C": lambda t: (abs(centre[1] - t[1])),
        "": lambda t: (abs(centre[1] - t[1]), abs(centre[0] - t[0])),
    }

    return time_prefs


def get_required(availability):
    required = dict([(p, 2) for p in availability])
    required["A"] = 3

    return required