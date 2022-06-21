# std
from __future__ import annotations
import os

# internal
from act.model.base import BaseObject
from act.model.target import Target


class Configuration(BaseObject):

    @property
    def filepath(self):
        return self.id

    @property
    def name(self):
        return os.path.basename(os.path.dirname(self.filepath))

    def get_target(self, name: str) -> Target:
        return Target(name, **self.data.get('targets', {}).get(name, {}) or {})

    @classmethod
    def load(cls, filepath: str) -> Configuration:
        with open(filepath, 'r') as fh:
            return Configuration.deserialize(filepath, fh.read())
