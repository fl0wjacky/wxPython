#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Sub-menu Example')
        p = wx.Panel(self)
        menu = wx.Menu()

        submenu = wx.Menu()
        submenu.Append(-1, 'Sub-item 1')
        submenu.Append(-1, 'Sub-item 2')
        menu.AppendMenu(-1, 'Sub-menu', submenu) # add sub menu

        menu.AppendSeparator()
        exit = menu.Append(-1, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, '&Menu')
        self.SetMenuBar(menuBar)

    def OnExit(self, evt):
        self.Close()

class App(wx.App):
    def OnInit(self):
        self.f = MyFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
