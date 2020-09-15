from collections import UserList


class Vial(UserList):

    def __init__(self, max_size, initlist=None):
        check_vial_arguments_meet_requirements(max_size, initlist)

        super().__init__(initlist)
        self.max_size = max_size


def check_vial_arguments_meet_requirements(max_size, initlist):
    assert max_size > 0
    if initlist is not None:
        assert len(initlist) <= max_size
