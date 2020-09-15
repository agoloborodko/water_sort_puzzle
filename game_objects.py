from collections import UserList
from exceptions import VialCannotAcceptThisException


class Vial(UserList):

    def __init__(self, max_size, initlist=None):
        check_vial_arguments_meet_requirements(max_size, initlist)

        super().__init__(initlist)
        self.max_size = max_size

    def can_accept(self, item):
        if len(self.data) < self.max_size:
            if len(self.data) == 0:
                return True
            elif item == self.data[-1]:
                return True
        return False

    def __raise_exception_if_not_appendable(self, item):
        if not self.can_accept(item):
            raise VialCannotAcceptThisException(f'Item {item} cannot be put in vial {self}')

    def append(self, item):
        self.__raise_exception_if_not_appendable(item)
        super().append(item)


def check_vial_arguments_meet_requirements(max_size, initlist):
    assert max_size > 0, 'max_size must be greater than zero!'
    assert isinstance(max_size, int), 'max_size must be integer!'

    if initlist is not None:
        assert len(initlist) <= max_size, 'initlist size cannot be greater than max_size!'


class VialBoard(UserList):

    def __init__(self, vial_list):
        check_board_arguments_meet_requirements(vial_list)
        super().__init__(vial_list)

    def move(self, donor_index, recipient_index):
        while self.__can_move(self[donor_index], self[recipient_index]):
            item = self[donor_index].pop()
            self[recipient_index].append(item)

    @staticmethod
    def __can_move(donor_vial, recipient_vial):
        if len(donor_vial) == 0:
            return False
        elif recipient_vial.can_accept(donor_vial[-1]):
            return True
        return False


def check_board_arguments_meet_requirements(vial_list):
    assert len(vial_list) > 1, 'VialBoard should contain at least 2 Vials!'
    first_vial = vial_list[0]
    for i in vial_list:
        assert isinstance(i, Vial), 'VialBoard elements all must be instances of Vial class!'
        assert first_vial.max_size == i.max_size
