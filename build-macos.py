import os
import py2app
import shutil
from setuptools import setup

def tree(src):
    data_files = []
    for (root, dirs, files) in os.walk(os.path.normpath(src)):
        files_list = [os.path.join(root, f) for f in files]
        if files_list:
            data_files.append((root, files_list))
    return data_files

if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist/index.app'):
    shutil.rmtree('dist/index.app')

ENTRY_POINT = ['src/index.py']
DATA_FILES = tree('gui')

OPTIONS = {
    'argv_emulation': False,
    'strip': False,
    'iconfile': 'src/assets/logo.icns',
    'packages': ['WebKit', 'Foundation', 'webview'],
    'plist': {
        'NSRequiresAquaSystemAppearance': False
    },
}

setup(
    app=ENTRY_POINT,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
