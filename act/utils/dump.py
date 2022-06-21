# internal
from act.model.configuration import Configuration


def dump(filepath: str, configuration: Configuration):
    with open(filepath, 'w') as fh:
        fh.write(configuration.serialize())
