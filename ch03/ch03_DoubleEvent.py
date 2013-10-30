#! /usr/bin/env python
# coding:utf-8

import wx

class DoubleEventFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame With Button',size=(300,100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel,id,'点击我',pos=(100,15))
        self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button)#1
        self.button.Bind(wx.EVT_LEFT_DOWN,self.OnMouseDown)#2
        
    def OnButtonClick(self,event):
        wx.MessageDialog(None,'see what happen?').ShowModal()
        self.panel.SetBackgroundColour('Blue')
        self.panel.Refresh()

    def OnMouseDown(self,event):
        self.button.SetLabel('再按一次！')
        event.Skip()#3

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = DoubleEventFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()
