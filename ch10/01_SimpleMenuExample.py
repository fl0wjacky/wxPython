#! /usr/bin/env python
# coding:utf-8

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Simple Menu Example")
        p = wx.Panel(self)
        menuBar = wx.MenuBar()  # Create a MenuBar
        menu = wx.Menu()        # Create a Menu
        menuBar.Append(menu,"Left Menu")    # Add Menu to MenuBar
        menu2 = wx.Menu()
        menuBar.Append(menu2,"Middle Menu")
        menu3 = wx.Menu()
        menuBar.Append(menu3,"Right Menu")
        self.SetMenuBar(menuBar)

class App(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()
