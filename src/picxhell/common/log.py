"""
Basic console log with colors and levels (info, error, warning, debug).
https://github.com/coolcornucopia/picxhell

MIT License

Copyright (c) 2022 coolcornucopia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


Example of use:
    import log
    log = log.Log(debug=True, name = __name__)
    log.i("This is an information message...")
    log.e("This is an error message...")
    log.w("This is a warning message...")
    log.d("This is a debug message...")

Note: We may use "logging" instead, see https://docs.python.org/3/howto/logging.html
      but it is nice to have less dependencies for micropython and "logging" is pretty big.

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/coolcornucopia/picxhell"


# For a color text:
# black 30, red 31, green 32, yellow 33, blue 34, magenta 35, cyan 36, white 37
# For a colored background:
# black 40, red 41, green 42, yellow 43, blue 44, magenta 45, cyan 46, white 47
# To remove the bold: replace the "1" by a "0" in "\033[1;34m"
# More colors and codes:
# https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
#
# TIPS: To remove all debug messages from all your modules, simply write in your main application:
#    import log
#    log.release_mode = True

release_mode = False


class console_colors:
    INFO    = "\033[1;34m"  # blue, bold
    ERROR   = "\033[1;31m"  # red, bold
    WARNING = "\033[1;33m"  # yellow, bold
    DEBUG   = "\033[1;35m"  # magenta, bold
    RESET   = "\033[0m"

class Log:
    """
    Basic console log with colors and levels (info, error, warning, debug).
    Example of use:
        import log
        log = log.Log(debug=True, name = "my_module_name")
        log.e("You should not do this!")
        log.d("This is a debug message...")
    Version: 1.0
    """

    def __init__(self, debug = False, name = None):
        self.debug = debug

        if name is not None:
            self.name = name
        else:
            # TODO does not work on micropython :-( please find a different way
            # avoid name = __name__ from the caller...
            import inspect
            from pathlib import Path
            self.name = Path(inspect.stack()[1].filename).stem

    def end_str(self):
        return self.name + ": " + console_colors.RESET

    def i(self, *args,**kwargs):
        print(console_colors.INFO + "INFO    " + self.end_str(), *args,**kwargs)

    def e(self, *args,**kwargs):
        print(console_colors.ERROR + "ERROR   " + self.end_str(), *args,**kwargs)

    def w(self, *args,**kwargs):
        print(console_colors.WARNING + "WARNING " + self.end_str(), *args,**kwargs)

    def d(self, *args,**kwargs):
        global release_mode
        print(release_mode)
        if self.debug and not release_mode:
            print(console_colors.DEBUG + "DEBUG   " + self.end_str(), *args,**kwargs)


