import time
import random
class EventSlots:
    Timer = 86399

    maps = [
        # Status = [3 = Nothing, 2 = Star Token, 1 = New Event]
        {
            'ID': random.choice([7,8,9,10,11,12,40,113,114,115,116,117,122,212]),
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': random.choice([14,32,33]),
            'Status': 2,
            'Ended': False,
            'Modifier': 2,
            'Tokens': 10
        },
        {
            'ID': random.choice([4,54,82,218,219]),
            'Status': 2,
            'Ended': False,
            'Modifier': 0,
            'Tokens': 10
        },

        {
            'ID': random.choice([53,137,146,216,217]),
            'Status': 2,
            'Ended': False,
            'Modifier': 2,
            'Tokens': 10
        }
    ]