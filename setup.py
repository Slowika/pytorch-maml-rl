# Copyright (C) 2018 Microsoft Corporation

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from setuptools import setup
from setuptools.command.install import install
from distutils.command.build import build
from distutils.core import setup, Extension
import os.path, sys

setup(name='maml-rl',
      version="0.0.1",
      install_requires=open("requirements.txt").read(),
      description='Reinforcement Learning with Model-Agnostic Meta-Learning (MAML)',
      author='Tristan Deleu',
      packages=['maml_rl'],
      include_package_data=True,
    #   package_dir={'jericho': 'jericho'},
    #   package_data={'jericho': ['libfrotz.so', 'clubfloyd_verb_counts.json']},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
          "Operating System :: POSIX :: Linux",
      ],
)