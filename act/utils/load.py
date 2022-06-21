# std
import os
from typing import List, Optional as Opt, Union

# internal
from act.utils.errors import ActRuntimeError
from act.utils import log
from act.model.configuration import Configuration
from act.model.tree import Node
from act.utils.funcs import compact, flatten


def load(dirpath: str = '.') -> Node:
    rootpath = _find_rootpath(dirpath)
    root_node = _build_tree(rootpath)
    return root_node


def _find_rootpath(dirpath: str) -> str:
    rootpath = None
    dirpath = os.path.abspath(dirpath)
    parts = dirpath.split(os.path.sep)
    for i in range(len(parts), 0, -1):
        dirpath = os.path.join(os.path.sep, *parts[:i])
        filepath = os.path.join(dirpath, 'act.yml')
        if os.path.isfile(filepath):
            rootpath = dirpath
    if rootpath is None:
        raise ActRuntimeError('Could not find root act.yml')
    log.debug(f'Root act.yml found: {rootpath}')
    return rootpath


def _build_tree(dirpath: str) -> Opt[Union[Node, List[Node]]]:
    filepath = os.path.join(dirpath, 'act.yml')
    if os.path.isfile(filepath):
        log.debug(f'act.yml found: {filepath}')
        node = Node(Configuration.load(filepath))
        children = compact(flatten([_build_tree(d) for d in _listdirs(dirpath)]))
        node.add_children(children)
        return node
    else:
        return compact(flatten([_build_tree(d) for d in _listdirs(dirpath)]))


def _listdirs(dirpath: str) -> List[str]:
    dirs: List[str] = []
    entry: os.DirEntry
    for entry in os.scandir(dirpath):
        if entry.is_dir():
            dirs.append(entry.path)
    return dirs
