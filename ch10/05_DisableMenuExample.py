#! /usr/bin/env python
# coding:utf-8

import wx

ID_SIMPLE = wx.NewId()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Enable|Disable Menu Example")
        p = wx.Panel(self)
        self.btn = wx.Button(p, -1, "Disable Item", (20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnToggleItem, self.btn)

        menu = wx.Menu()
        menu.Append(ID_SIMPLE, 'Simple menu item')
        self.Bind(wx.EVT_MENU, self.OnSimple, id = ID_SIMPLE)

        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, id = wx.ID_EXIT)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

    def OnSimple(self, evt):
        wx.MessageBox("You selected the simple menu item")

    def OnExit(self, evt):
        self.Close()

    def OnToggleItem(self, evt):
        menuBar = self.GetMenuBar()
        enabled = menuBar.IsEnabled(ID_SIMPLE)
        menuBar.Enable(ID_SIMPLE, not enabled)
        self.btn.SetLabel((enabled and "Enable" or "Disable") + " Item")

class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        return True
if __name__ == "__main__":
    App().MainLoop()
