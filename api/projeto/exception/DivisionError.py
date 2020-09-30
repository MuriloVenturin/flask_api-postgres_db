from builtins import ZeroDivisionError

from api.arquitetura.projeto.constants import Message


class DivisionException(Exception):

    def __init__(self, msg):
        super().__init__(msg)