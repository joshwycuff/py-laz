# std
import os
import subprocess
from typing import List

# internal
from act.utils.contexts import in_dir
from act.model.action import Action
from act.model.target import Target
from act.utils.templates import expand


class Act:

    def __init__(self, target: Target, args: List[str]):
        target.push(expand(target.data))
        self.target = target
        self.args = expand(args, target.data)
        self.action = Action.new(self.target, self.args)

    def act(self):
        with in_dir(self.target.data['dirpath']):
            self.action.run()
