import os
import py2app
import shutil

from distutils.core import setup

def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files))
        for (root, dirs, files) in os.walk(os.path.normpath(src))]


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
    'resources': DATA_FILES
}

setup(
    app=ENTRY_POINT,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
