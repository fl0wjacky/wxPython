#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Toggle Items Example")
        p = wx.Panel(self)
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        exit = menu.Append(-1, "Exit")
        self.Bind(wx.EVT_MENU, self.OnExit, exit)
        menuBar.Append(menu, 'Menu')

        menu = wx.Menu()
        menu.AppendCheckItem(-1, "Check Item 1")
        menu.AppendCheckItem(-1, "Check Item 2")
        menu.AppendCheckItem(-1, "Check Item 3")
        
        menu.Append(-1,'Check Item 4',kind = wx.ITEM_CHECK)

        menu.AppendSeparator()
        menu.AppendRadioItem(-1, "Radio Item 1")
        menu.AppendRadioItem(-1, "Radio Item 2")
        menu.AppendRadioItem(-1, "Radio Item 3")
        
        menu.Append(-1, "Radio Item 4", kind = wx.ITEM_RADIO)

        menuBar.Append(menu, "Toggle Items")

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
