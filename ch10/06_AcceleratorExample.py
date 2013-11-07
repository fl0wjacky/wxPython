#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Accelerator Example")
        p = wx.Panel(self)
        menu = wx.Menu()
        simple = menu.Append(-1, "Simple &menu item") # Creating a mnemonic
        accel = menu.Append(-1, '&Accelerated\tCtrl+A') # Creating an accelerator

        menu.AppendSeparator()
        exit = menu.Append(-1, "E&xit")

        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnAccelerated, accel)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "&Menu")
        self.SetMenuBar(menuBar)

        ab = wx.AcceleratorTable([(wx.ACCEL_CTRL,ord('Q'),exit.GetId())])   #这种方式创建的加速器在CentOS（gnome)下无效，在Windows下有效
        self.SetAcceleratorTable(ab)

    def OnSimple(self, evt):
        wx.MessageBox("You selected the simple menu item")

    def OnAccelerated(self, evt):
        wx.MessageBox('You selected the accelerated menu item')

    def OnExit(self, evt):
        self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
