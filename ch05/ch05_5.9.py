#! /usr/bin/env python
# -*- coding:utf-8 -*-
import wx
import wx.grid
from generictable import GenericTable

data = (("Bob","Dernier"),("Ryne","Sandberg"),
        ("Gary","Matthews"),("Leon","Durham"),
        ("Keith","Moreland"),("Ron","Cey"),
        ("Jody","Davis"),("Larry","Bowa"),
        ("Rick","Sutcliffe"))
colLabels = ("Last","First")
rowLabels = ("CF","2B","LF","1B","RF","3B","C","SS","P")

class SimpleGrid(wx.grid.Grid):
    def __init__(self,parent):
        wx.grid.Grid.__init__(self,parent,-1)
        tableBase = GenericTable(data,rowLabels,colLabels)
        self.SetTable(tableBase)

class TestFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"A Grid",size=(275,275))
        self.grid = SimpleGrid(self)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame(None)
    frame.Show()
    app.MainLoop()
