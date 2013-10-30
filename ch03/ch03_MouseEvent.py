#! /usr/bin/env python
# -*- coding:utf-8 -*-
import wx

class MouseEventFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Frame Wtih Button',size=(300,100))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel,label='别过来',pos=(100,15))
        #self.Bind(wx.EVT_BUTTON,self.OnButtonClick,self.button)
        #self.button.Bind(wx.EVT_ENTER_WINDOW,self.OnEnterWindow)
        #self.button.Bind(wx.EVT_LEAVE_WINDOW,self.OnLeaveWindow)

    def OnButtonClick(self,event):
        self.panel.SetBackgroundColour('Red')
        self.panel.Refresh()

    def OnEnterWindow(self,event):
        self.button.SetLabel('走开')
        event.Skip()
    def OnLeaveWindow(self,event):
        self.button.SetLabel('别过来')
        event.Skip()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MouseEventFrame(None,-1)
    app.Bind(wx.EVT_BUTTON,frame.OnButtonClick,frame.button)
    frame.Show()
    app.MainLoop()
