import winreg as wrg

location = wrg.HKEY_LOCAL_MACHINE

soft = wrg.OpenKeyEx(location, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer")
key_1 = wrg.CreateKey(soft, "Shell Icons")

wrg.SetValueEx(key_1, "29", 0, wrg.REG_SZ,
               "%windir%\System32\shell32.dll,-50")
  
if key_1:
    wrg.CloseKey(key_1)