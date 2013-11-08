#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Popup Menu Example")
        self.panel = p = wx.Panel(self)
        menu = wx.Menu()
        exit = menu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "Menu")
        self.SetMenuBar(menuBar)

        wx.StaticText(p, -1, "Right-click on the panel to show a popup menu", (25, 25))

        self.popupmenu = wx.Menu() # Create a menu
        for text in "one two three four five".split(): # fill the menu
            item = self.popupmenu.Append(-1, text)
            self.Bind(wx.EVT_MENU, self.OnPopupItemSelected, item)
        self.popupmenu.SetTitle('I am the menu title')
        p.Bind(wx.EVT_CONTEXT_MENU, self.OnShowPopup) # bind a display menu event

    def OnShowPopup(self, evt): # popup the menu handler
        pos = evt.GetPosition()
        pos = self.panel.ScreenToClient(pos)
        self.panel.PopupMenu(self.popupmenu, pos)   #PopupMenuXY() method will popup the menu at the fixed position if you don't use the default values

    def OnPopupItemSelected(self, evt):
        item = self.popupmenu.FindItemById(evt.GetId())
        text = item.GetText()
        wx.MessageBox("You selected item '%s'" % text)

    def OnExit(self, evt):
        self.Close()

class App(wx.App):
    def OnInit(self):
        self.f = MyFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
