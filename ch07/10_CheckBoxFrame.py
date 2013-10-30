#! /usr/bin/env python
# coding:utf-8

import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Checkbox Example',size = (150,200))
        self.panel = wx.Panel(self,-1)
        self.c1 = wx.CheckBox(self.panel,-1,'Alpha',(35,40),(150,20))
        self.c2 = wx.CheckBox(self.panel,-1,'Beta',(35,60),(150,20))
        self.c3 = wx.CheckBox(self.panel,-1,'Gamma',(35,80),(150,20))

class App(wx.App):
    def OnInit(self):
        self.frame = CheckBoxFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
