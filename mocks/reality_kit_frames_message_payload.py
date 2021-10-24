import json
import random

def get_random_display_pattern():
    payload = []
    for _ in range(64):
        light = []
        for __ in range(3):
            light.append(random.randint(0, 255))
        payload.append(light)
    return payload


class RealityKitFrame(object):

    def __init__(self, time_to_live, display):
        self.time_to_live = time_to_live
        self.display = display

    def __dict__(self):
        return {
            "time_to_live": self.time_to_live,
            "display": self.display
        }


if __name__ == "__main__":
    payload = []
    priority = random.randint(0, 3)
    for n in range(3):
        payload.append(
            RealityKitFrame(
                random.randint(0, 50),
                get_random_display_pattern()
            ).__dict__()
        )
    print(json.dumps({
        "priority": priority,
        "payload": payload
    }))
