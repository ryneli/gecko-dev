# Default configuration as used by Mozmill CI (Jenkins)

import os
import sys

import mozharness


external_tools_path = os.path.join(
    os.path.abspath(os.path.dirname(os.path.dirname(mozharness.__file__))),
    'external_tools',
)

config = {
    'env': {
        'PIP_TRUSTED_HOST': 'pypi.pub.build.mozilla.org',
    },

    # Don't use any kind of proxxy support
    'proxxy': {},

    # General local variable overwrite
    'exes': {
        'gittool.py': [
            # Bug 1227079 - Python executable eeded to get it executed on Windows
            sys.executable,
            os.path.join(external_tools_path, 'gittool.py')
        ],
        'hgtool.py': [
            # Bug 1227079 - Python executable eeded to get it executed on Windows
            sys.executable,
            os.path.join(external_tools_path, 'hgtool.py')
        ],
    },

    # PIP
    'find_links': ['http://pypi.pub.build.mozilla.org/pub'],
    'pip_index': False,

    # mozcrash support
    'download_minidump_stackwalk': True,
    'download_symbols': 'ondemand',
    'download_tooltool': True,
}
