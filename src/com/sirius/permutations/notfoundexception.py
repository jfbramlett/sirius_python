
class NotFoundException(Exception) :
    """
    Exception used when we can't find a requested resource
    """

    def __init__(self, entityId):
        self.entityId = entityId