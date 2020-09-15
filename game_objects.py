from collections import UserList


class Vial(UserList):

    def __init__(self, max_size, initlist=None):
        if initlist is not None:
            assert len(initlist) <= max_size
        super().__init__(initlist)
        self.max_size = max_size
