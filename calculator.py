# try:
#     from robot.libraries.BuiltIn import BuiltIn
#     from robot.libraries.BuiltIn import _Misc
#     import robot.api.logger as logger
#     from robot.api.deco import keyword
#     ROBOT = False
# except Exception:
#     ROBOT = False

class Calculator:
    # @keyword
    def add(self, a, b):
        return int(a)+int(b)

cal =Calculator()