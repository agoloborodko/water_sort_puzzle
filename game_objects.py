import copy
from functools import wraps
from collections import UserList
from exceptions import VialCannotAcceptThisException, VialIsFullException


class Vial(UserList):

    def __init__(self, max_size, initlist=None):
        check_vial_arguments_meet_requirements(max_size, initlist)

        super().__init__(initlist)
        self.max_size = max_size

    def is_full(self):
        if len(self.data) < self.max_size:
            return False
        else:
            return True

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def can_accept(self, item):
        if self.is_empty():
            return True
        if not self.is_full():
            if item == self.data[-1]:
                return True
        return False

    def __raise_exception_if_full(self):
        if self.is_full():
            raise VialIsFullException('Vial is full and cannot accept more items')

    def append(self, item):
        self.__raise_exception_if_full()
        super().append(item)

    def count_unique(self):
        return len(set(self))


def check_vial_arguments_meet_requirements(max_size, initlist):
    assert max_size > 0, 'max_size must be greater than zero!'
    assert isinstance(max_size, int), 'max_size must be integer!'

    if initlist is not None:
        assert len(initlist) <= max_size, 'initlist size cannot be greater than max_size!'


def log_move(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        self.path.append(tuple(method_args))
        return method_output
    return _impl


def reset_path(method):
    @wraps(method)
    def _impl(self, *method_args, **method_kwargs):
        method_output = method(self, *method_args, **method_kwargs)
        self.path = []
        return method_output
    return _impl


class VialBoard(UserList):

    path = []

    @reset_path
    def __init__(self, vial_list):
        vial_list = self.__make_vials_from_lists(vial_list)
        check_board_arguments_meet_requirements(vial_list)
        super().__init__(vial_list)
        self.init_data = copy.deepcopy(self.data)

    def __str__(self):
        result = ''
        size = self[0].max_size
        for line in range(size-1, -1, -1):
            for vial in self:
                if len(vial) > line:
                    result += f'|{vial[line]:->3}|'
                else:
                    result += f'|---|'
            result += '\n'
        return result

    @staticmethod
    def __can_move(donor_vial, recipient_vial):
        if donor_vial.is_empty():
            return False
        elif recipient_vial.can_accept(donor_vial[-1]):
            return True
        return False

    @staticmethod
    def __make_vials_from_lists(input_list):
        max_size = 2
        result = []
        for i in input_list:
            assert isinstance(i, (Vial, list))
            if len(i) > max_size:
                max_size = len(i)
        for i in input_list:
            vial = Vial(max_size, i)
            result.append(vial)
        return result

    def get_set_of_items(self):
        s = set()
        for vial in self:
            s = s.union(vial)
        return s

    @log_move
    def __make_simple_move(self, donor_index, recipient_index):
        item = self[donor_index].pop()
        self[recipient_index].append(item)

    def move(self, donor_index, recipient_index):
        while self.__can_move(self[donor_index], self[recipient_index]):
            self.__make_simple_move(donor_index, recipient_index)

    @reset_path
    def restart_game(self):
        self.data = copy.deepcopy(self.init_data)

    def solved(self):
        game_items = set()
        for vial in self:
            if not vial.is_empty():
                if vial.count_unique() > 1:
                    return False
                elif vial[0] in game_items:
                    return False
                game_items.add(vial[0])
        return True

    # TODO: add a way to memorize path and do step-backs


def check_board_arguments_meet_requirements(vial_list):
    assert len(vial_list) > 1, 'VialBoard should contain at least 2 Vials!'
    first_vial = vial_list[0]
    for i in vial_list:
        assert isinstance(i, Vial), 'VialBoard elements all must be instances of Vial class!'
        assert first_vial.max_size == i.max_size
