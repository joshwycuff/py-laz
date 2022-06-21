# std
from typing import List

# internal
from act.model.tree import Node
from act.model.path import Path
from act.model.resolver import Resolver
from act.model.target import Target


class Runner:

    def __init__(self, root_node: Node, args: List[str]):
        self.root_node = root_node
        self.path = Path(args[0])
        self.args = args[1:]

    def resolve(self) -> List[Target]:
        resolver = Resolver(self.root_node, self.path)
        return resolver.resolve()

    def run(self):
        targets = self.resolve()
        for target in targets:
            print(target.json())
