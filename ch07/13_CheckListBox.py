#! /usr/bin/env python
# coding:utf-8
'''为什么触发一个wx.EVT_CHECKLISTBOX后会触发一个wx.EVT_LISTBOX触发器'''
import wx

class CheckListFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Check List Box Example",size=(400,400))
        self.panel = wx.Panel(self,-1)

        self.count = 0
        self.choices = ['a','b','c','d','e']
        self.cl = wx.CheckListBox(self.panel,-1,pos=(10,10),choices=self.choices)
        self.cl.Bind(wx.EVT_LISTBOX,self.OnListBox)
        self.cl.Bind(wx.EVT_CHECKLISTBOX,self.OnCheckListBox)

    def OnListBox(self,event):
        self.count += 1
        print('list box %d' % self.count)
        #event.Skip(0)

    def OnCheckListBox(self,event):
        self.count += 1
        print('Check List Box %d' % self.count)

class App(wx.App):
    def OnInit(self):
        self.frame = CheckListFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
