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

DATA_FILES = tree('dist')
OPTIONS = {
    'argv_emulation': False,
    'strip': True,
    'iconfile': 'src/assets/logo.icns',
    'includes': ['WebKit', 'Foundation', 'webview', 'pkg_resources.py2_warn']
}

setup(
    app=ENTRY_POINT,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
