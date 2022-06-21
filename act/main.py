# std
import sys

# internal
from act.utils import log


def main():
    log.debug(sys.argv[1:])
    if len(sys.argv) == 2 and (sys.argv[1] == 'version' or sys.argv[1] == '--version'):
        from act.cli.subcommands.version import version
        version()
    else:
        from act.cli.root import root
        root()


if __name__ == '__main__':
    cmd = 'act version'
    sys.argv = cmd.split(' ')
    main()
