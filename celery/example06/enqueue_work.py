# vim: set fileencoding=utf-8

from tasks import add, multiply

add.apply_async((1, 2), link=multiply.s(3))
