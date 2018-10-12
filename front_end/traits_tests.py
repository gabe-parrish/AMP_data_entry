# ===============================================================================
# Copyright 2018 gabe-parrish
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= standard library imports ========================
import os
# os.environ['QT_API'] = 'pyqt5'
os.environ['ETS_TOOLKIT'] = 'wx'

from traitsui.toolkit import *

from traits.trait_base import ETSConfig
from pyface.base_toolkit import Toolkit, find_toolkit
from traits.api import HasTraits, Int, Str, Property
# from traitsui.api import *
from subprocess import call

"""if you have trouble with the toolkit you need to check it in the terminal. this can be done in terminal in the current env: $ export ETS_TOOLKIT=qt4"""

# ============= local library imports ===========================

print(os.environ)
# print(ETSConfig.toolkit)
# ETSConfig.toolkit = 'qt4'
os.environ['ETS_TOOLKIT'] = 'wx'
# call('export ETS_TOOLKIT=qt4', shell=True)
print(os.environ)

# os.environ['ETS_TOOLKIT'] = 'qt4'
class Calculator(HasTraits):

    # toolkit('qt4')

    value1 = Int()
    value2 = Int()

    sum = Property(Int, depends_on='value1, value2')

    def _get_sum(self):

        return self.value1 + self.value2

def main():
    """Tests traits"""
    # print(os.environ['ETS_TOOLKIT'])
    print("toolkit i'm trying to use", ETSConfig.toolkit)
    # ETSConfig.toolkit = 'wx'
    # sys.environment("export ETS_TOOLKIT=qt4", shell=True)
    # ETSConfig.enable_toolkit
    Calculator().configure_traits()

    # calc.configure_traits()

if __name__ == "__main__":
    main()