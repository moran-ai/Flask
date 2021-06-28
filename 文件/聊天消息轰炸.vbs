Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.AppActivate"联系人名字"
for i=1 to 轰炸次数
WScript.Sleep 500
WshShell.SendKeys"^v"
WshShell.SendKeys i
WshShell.SendKeys "%s"
Next

