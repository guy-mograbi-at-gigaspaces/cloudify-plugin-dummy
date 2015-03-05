########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.


from setuptools import setup, find_packages


install_requires = [
    'cloudify-docker-plugin'
]


setup(
    name='cloudify-plugin-dummy',
    version='0.0.0',
    author='Guy Mograbi',
    author_email='guym@gigaspaces.com',
    packages=find_packages(),
    license='LICENSE',
    description='a dummy plugin',
    zip_safe=False,
    install_requires=install_requires
)
