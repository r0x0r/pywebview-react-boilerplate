import os
import threading
import webview

from time import time


class Api:
    def fullscreen(self):
        print('fullscreen')
        webview.windows[0].toggle_fullscreen()

    def save_content(self, content):
        print(1)
        filename = webview.windows[0].create_file_dialog(webview.SAVE_DIALOG)
        print(filename)

        if not filename:
            return

        with open(filename, 'w') as f:
            f.write(content)

    def ls(self):
        return os.listdir('.')


def get_entrypoint():
    def exists(path):
        return os.path.exists(os.path.join(os.path.dirname(__file__), path))

    if exists('../dist/index.html'): # unfrozen development
        return '../dist/index.html'

    if exists('../Resources/dist/index.html'): # frozen py2app
        return '../Resources/dist/index.html'

    if exists('../dist/index.html'): # TODO pyinstaller
        return '../dist/index.html'

    raise Exception('No index.html found')


def set_interval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator



entry = get_entrypoint()

@set_interval(1)
def update_ticker():
     webview.windows[0].evaluate_js('window.pywebview.setTicker("%d")' % time())


if __name__ == '__main__':
    window = webview.create_window('pywebview-react boilerplate', entry, js_api=Api())
    webview.start(update_ticker, debug=True)
