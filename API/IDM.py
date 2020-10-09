import winreg

class IDM():
    """docstring for IDM"""

    def __init__(self):
        super(IDM, self).__init__()
        self.typeLib = r"SOFTWARE\Classes\Wow6432Node\TypeLib"

    def UUID(self):
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.typeLib) as location:
            for i in range(0, winreg.QueryInfoKey(location)[0]):
                try:
                    sub = winreg.EnumKey(location, i)
                    res = winreg.OpenKey(location, sub)
                    subs = winreg.EnumKey(res, 0)
                    result = winreg.OpenKey(res, subs)
                    if winreg.QueryValue(result, "") == "IDMan 1.0 Type Library":
                        return sub
                except OSError:
                    continue
