#! /usr/bin/env python 
# coding:utf-8

import wx

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Test',(100,100),(200,200))
        self.panel = wx.Panel(self,-1)
        self.button = wx.Button(self.panel,-1,'Kick me',(10,10),name='xbutton')
        self.button.SetDefault()
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)

    def OnClick(self,event):
        #item = wx.FindWindowByLabel('Kick me')
        #item = wx.FindWindowByName('xbutton',self.panel)
        id = event.GetId()
        item = wx.FindWindowById(id,self.panel)
        if item.GetLabel() != 'Kick me':
            item.SetLabel('Kick me')
        else:
            item.SetLabel('em kciK')

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame()
    frame.Show()
    app.MainLoop()
