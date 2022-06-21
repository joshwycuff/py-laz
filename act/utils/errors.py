class ActError(Exception):
    pass


class ActValueError(ActError, ValueError):
    pass


class ActTypeError(ActError, TypeError):
    pass


class ActRuntimeError(ActError, RuntimeError):
    pass
