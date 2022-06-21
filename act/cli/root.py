# std
import argparse
import sys
from typing import List, Tuple

# internal
from act.utils.errors import ActRuntimeError
from act.utils.load import load
from act.utils.logging import get_logger
from act.model.runner import Runner


def root():
    cli_args, act_args = _split_args()
    if len(act_args) == 0:
        raise ActRuntimeError('No path provided')
    elif len(act_args) == 1:
        raise ActRuntimeError('No arguments provided')
    cli_args = parser.parse_args(cli_args)
    get_logger(verbosity=cli_args.verbose)
    root_node = load()
    runner = Runner(root_node, act_args)
    runner.run()


def _split_args() -> Tuple[List[str], List[str]]:
    for i, s in enumerate(sys.argv):
        if i > 0 and not s.startswith('-'):
            return sys.argv[1:i], sys.argv[i:]
    return sys.argv[1:], []


parser = argparse.ArgumentParser(description='act cli')

parser.add_argument('--verbose', '-v', action='count', default=0, help='Set logging verbosity')
