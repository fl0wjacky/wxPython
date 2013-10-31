#! /usr/bin/env python
# coding:utf-8

import wx

class ScrollbarFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Scrollbar Example',size=(300,200))
        self.scroll = wx.ScrolledWindow(self,-1)
        self.scroll.SetScrollbars(1,1,600,400)
        self.button = wx.Button(self.scroll,-1,"Scroll Me",pos = (50,20))
        self.Bind(wx.EVT_BUTTON,self.OnClickTop,self.button)
        self.button2 = wx.Button(self.scroll,-1,"Scroll Back",pos = (400,250))
        self.Bind(wx.EVT_BUTTON,self.OnClickBotton,self.button2)
        self.scroll.SetScrollRate(2,2)

    def OnClickTop(self,event):
        self.scroll.Scroll(600,400)

    def OnClickBotton(self,event):
        self.scroll.Scroll(1,1)

class App(wx.App):
    def OnInit(self):
        self.frame = ScrollbarFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
