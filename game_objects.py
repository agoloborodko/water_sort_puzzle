from collections import UserList
from exceptions import VialCannotAcceptThisException

class Vial(UserList):

    def __init__(self, max_size, initlist=None):
        check_vial_arguments_meet_requirements(max_size, initlist)

        super().__init__(initlist)
        self.max_size = max_size

    def is_appendable(self, item):
        if len(self.data) < self.max_size:
            if len(self.data) == 0:
                return True
            elif item == self.data[-1]:
                return True
        return False

    def __raise_exception_if_not_appendable(self, item):
        if not self.is_appendable(item):
            raise VialCannotAcceptThisException(f'Item {item} cannot be put in vial {self}')

    def append(self, item):
        self.__raise_exception_if_not_appendable(item)
        super().append(item)


def check_vial_arguments_meet_requirements(max_size, initlist):
    assert max_size > 0, 'max_size must be greater than zero!'
    assert isinstance(max_size, int), 'max_size must be integer!'

    if initlist is not None:
        assert len(initlist) <= max_size, 'initlist size cannot be greater than max_size!'
