def dBrickId(brickId):
    """Return box id if valid, raise an exception in other case"""
    if brickId >= 0 and brickId <= 15:
        return brickId
    else:
        raise ValueError(
            '{} is not a valid Brick Id, Brick Id must be between 0-15'.format(
                brickId))


def dBoxId(boxId):
    """Return box id if valid, raise an exception in other case"""
    if boxId >= 0:
        return boxId
    else:
        raise ValueError(
            '{} is not a valid Box Id, Box Id must be >= 0'.format(boxId))


def dRackId(rackId):
    """Return rack id if valid, raise an exception in other case"""
    if rackId >= 0:
        return rackId
    else:
        raise ValueError(
            '{} is not a valid Rack Id, Rack Id must be >= 0'.format(rackId))
