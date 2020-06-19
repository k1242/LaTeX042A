Set s = CreateObject("Wscript.Shell")
Wscript.Sleep 400
s.sendkeys "%{TAB}"
Wscript.Sleep 200
s.sendkeys "%{F4}"
Wscript.Sleep 200
s.SendKeys "{RIGHT}"
Wscript.Sleep 200
s.SendKeys "{ENTER}"