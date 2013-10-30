#! /usr/bin/env python
# -*- coding:utf-8 -*-

import wx
from ch06_SketchWindow import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"Sketch Frame",size=(800,600))
        self.sketch = SketchWindow(self,-1)
        self.sketch.Bind(wx.EVT_MOTION,self.OnSketchMotion)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def OnSketchMotion(self,event):
        self.statusbar.SetStatusText(str(event.GetPositionTuple()))
        event.Skip()
        self.statusbar.SetStatusText("Current Pts:%s" % len(self.sketch.curLine),1)
        self.statusbar.SetStatusText("Line Count:%s" % len(self.sketch.lines),2)

class App(wx.App):
    def OnInit(self):
        self.frame = SketchFrame(None)
        self.frame.Show(True)
        return True
    

if __name__ == '__main__':
    app = App()
    app.MainLoop()
