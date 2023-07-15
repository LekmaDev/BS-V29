import string
import random

class Helpers:
    game1 = [{"LogicGameObjects": 2},{"id": 1, "hp": 3000,"immun": True,"UltiPress": False,"UltiCharge": 0,"battleX": 3150,"battleY": 6725,"angle": 270},{"id": 228, "hp": 3000, "immun": True, "UltiPress": False, "UltiCharge": 0,"battleX": 3150,"battleY": 3725,"angle": 180}]
    rooms = []
    online = 0
    freepass = 0
    buyepass = 0
    udp_port = 0

    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))
    def randomID(self):
        length = 9
        return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))
    def randomClubID(self):
        length = 9
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))