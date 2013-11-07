#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Find Item Example')
        p = wx.Panel(self)
        self.txt = wx.TextCtrl(p, -1, 'new item')
        btn = wx.Button(p, -1, 'Add Menu Item')
        self.Bind(wx.EVT_BUTTON, self.OnAddItem, btn)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.txt, 0, wx.ALL, 20)
        sizer.Add(btn, 0, wx.TOP | wx.RIGHT, 20)
        p.SetSizer(sizer)

        self.CreateStatusBar()

        self.menu = menu = wx.Menu()
        simple = menu.Append(-1, 'Simple menu item','I am the original simple menu item')
        menu.AppendSeparator()
        exit = menu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnSimple, simple)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, 'Menu')
        self.SetMenuBar(menuBar)

    def OnSimple(self, event):
        wx.MessageBox("You selected the simple menu item")

    def OnExit(self,evt):
        self.Close()

    def OnAddItem(self, evt):
        item = self.menu.Append(-1, self.txt.GetValue())
        self.Bind(wx.EVT_MENU, self.OnNewItemSelected, item)

    def OnNewItemSelected(self, evt):
        item = self.GetMenuBar().FindItemById(evt.GetId())
        text = item.GetText()
        wx.MessageBox("You selected the '%s' item" % text)

class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
