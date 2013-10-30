#! /usr/bin/env python
# coding:utf-8

import wx
from ch06_SketchWindow import *

class SketchApp(wx.App):
    def OnInit(self):
        bmp = wx.Image("splash.png").ConvertToBitmap()
        wx.SplashScreen(bmp,wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,             5000,None,-1)
        wx.Yield()
        frame = SketchFrame(None)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

if __name__ == "__main__":
    app = SketchApp()
    app.MainLoop()
