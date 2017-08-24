class PIECE(object):
    TOP = 0
    BOTTOM = 1
    FOOTWEAR = 2
    HEADGEAR = 3
    JACKET = 4
    ACCESSORY = 5
    OTHER = 6
    PIECE = (
        (TOP, 'Top'),
        (BOTTOM, 'Bottom'),
        (FOOTWEAR, 'Footwear'),
        (HEADGEAR, 'Headgear'),
        (JACKET, 'Jacket'),
        (ACCESSORY, 'Accessory'),
        (OTHER, 'Other'),
    )

    @classmethod
    def tostring(cls, val):
        # Convert to Python 3
        for k, v in vars(cls).items():
            if v == val:
                return k

    @classmethod
    def fromstring(cls, input_string):
        return getattr(cls, input_string.upper(), None)


class SEASON(object):
    WINTER = 0
    SUMMER = 1
    FALL = 2
    SPRING = 3
    ANY = 4
    SEASON = (
        (WINTER, 'Winter'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
        (SPRING, 'Spring'),
        (ANY, 'Any'),
    )

    @classmethod
    def tostring(cls, val):
        # Convert to Python 3
        for k, v in vars(cls).items():
            if v == val:
                return k

    @classmethod
    def fromstring(cls, input_string):
        return getattr(cls, input_string.upper(), None)


class GENDER(object):
    MALE = 0
    FEMALE = 1
    NEUTRAL = 2
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NEUTRAL, 'Neutral'),
    )

    @classmethod
    def tostring(cls, val):
        # Convert to Python 3
        for k, v in vars(cls).items():
            if v == val:
                return k

    @classmethod
    def fromstring(cls, input_string):
        return getattr(cls, input_string.upper(), None)
