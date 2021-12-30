# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nox

FLAKE8_COMMON_ARGS = [
    '--show-source',
    '--builtin=gettext',
    '--max-complexity=20',
    '--exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py',
    '--ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202',
    '--max-line-length=88',
    '.',
]


@nox.session(python=['2.7', '3.6', '3.9'])
def tests(session):
    """
    nox test session
    """
    session.install('pytest', 'blinker', 'flask', 'google-cloud-translate')
    session.run('pytest')


@nox.session(python=['2.7', '3.6', '3.9'])
def lint(session):
    """
    nox lint session
    """
    session.install('flake8')
    args = FLAKE8_COMMON_ARGS
    session.run('flake8', *args)
