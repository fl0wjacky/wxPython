#! /usr/bin/env python

import wx
import wx.py.images as images

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(300,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()#1
        toolbar = self.CreateToolBar()#2
        toolbar.AddSimpleTool(wx.NewId(),images.getPyBitmap(),"New","Long help for 'New'")#3
        toolbar.Realize()#4
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1,"&File")
        menu2 = wx.Menu()
        #6
        menu2.Append(wx.NewId(),"&Copy","Copy in status bar")
        menu2.Append(wx.NewId(),"C&ut","")
        menu2.Append(wx.NewId(),"Paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"&Options...","Display Options")
        menuBar.Append(menu2,"&Edit")
        self.SetMenuBar(menuBar)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id = -1)
    frame.Show()
    app.MainLoop()
