#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Simple Menu Example")
        p = wx.Panel(self)
        self.CreateStatusBar()
        menu = wx.Menu()
        simple = menu.Append(-1, "Simple menu item", 'This is some help text')
        menu.AppendSeparator()
        exit = menu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Simple Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self, evt):
        wx.MessageBox("You selected the simple menu item")

    def OnExit(self, evt):
        self.Close()

class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
