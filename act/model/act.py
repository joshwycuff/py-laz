# std
import os
import subprocess
from typing import List

# internal
from act.utils.contexts import in_dir
from act.model.action import Action
from act.model.target import Target


class Act:

    def __init__(self, target: Target, args: List[str]):
        self.target = target
        self.args = args

    def act(self):
        with in_dir(self.target.data['dirpath']):
            self._act()

    def _act(self):
        subprocess.run(self.args)
