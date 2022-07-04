# std
import os
from typing import Dict, Union

# internal
from laz.utils.errors import LazValueError, LazError
from laz.utils.types import Data
from laz.utils.contexts import with_environ
from laz.model.action import Action
from laz.model.configuration import Configuration
from laz.model.target import Target
from laz.plugins.plugin import Plugin


class AwsPlugin(Plugin):

    def before_all(self):
        env = {}
        aws_profile = self.context.data.get('aws', {}).get('profile')
        if aws_profile is not None:
            env['AWS_PROFILE'] = aws_profile
        aws_region = self.context.data.get('aws', {}).get('region')
        if aws_region is not None:
            env['AWS_DEFAULT_REGION'] = aws_region
        if env:
            self.context.push({'env': env})


class AwsAction(Action):

    def run(self):
        if isinstance(self.run_data['aws'], dict) and 'assume_role' in self.run_data['aws']:
            self._assume_role()
        else:
            raise LazValueError(f'Invalid aws plugin action')

    def _assume_role(self):
        import boto3
        aws: dict = self.run_data['aws']
        kwargs: Dict[str, str] = aws['assume_role']
        if 'RoleSessionName' not in kwargs:
            kwargs['RoleSessionName'] = os.environ['USER']
        with with_environ(self.context.data.get('env', {})):
            sts = boto3.client('sts')
            response = sts.assume_role(**kwargs)
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        if status_code >= 300:
            raise LazError(f'Assume Role Error: HTTPStatusCode {status_code}')
        credentials = response['Credentials']
        env = {
            'AWS_ACCESS_KEY_ID': credentials['AccessKeyId'],
            'AWS_SECRET_ACCESS_KEY': credentials['SecretAccessKey'],
            'AWS_SESSION_TOKEN': credentials['SessionToken'],
        }
        self.context.push({'env': env})


    @classmethod
    def is_handler(cls, context: Union[Configuration, Target], run_data: Data) -> bool:
        return isinstance(run_data, dict) and 'aws' in run_data
