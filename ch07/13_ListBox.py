#! /usr/bin/env python
# coding:utf-8

import wx

class ListBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'List Box Example',size = (200,200))
        self.panel = wx.Panel(self,-1)
        self.count = 0
        self.sampleList = ['zero','one','two','three','four','five',
                        'six','seven','eight','nine','ten','eleven',
                        'twelve','thirteen','fourteen']

        self.lb = wx.ListBox(self.panel,-1,(20,20),(80,120),
                self.sampleList,wx.LB_SINGLE)
        self.lb.SetSelection(3)
        self.Bind(wx.EVT_LISTBOX,self.OnList,self.lb)

    def OnList(self,event):
        self.count += 1
        print('Done %d' % self.count)

class App(wx.App):
    def OnInit(self):
        self.frame = ListBoxFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
