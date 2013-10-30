#! /usr/bin/env python

import wx
import sys
import time

class Frame(wx.Frame):
    def  __init__(self, parent, id, title):
        print("Frame __init__")
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self, redirect = True, filename = None):
        print("App __init__")
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print('OnInit')
        self.frame = Frame(parent = None, id = -1, title = "startup")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print sys.stderr, "A pretend error message"
        return True

    def OnExit(self):
        print("OnExit")

if __name__ == "__main__":
    app = App(True, "output")
    print("before MainLoop")
    app.MainLoop()
    print("After MainLoop")
