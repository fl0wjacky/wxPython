#! /usr/bin/env python
# coding:utf-8

import wx

class RadioButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Radio Example',size = (200,200))
        self.panel = wx.Panel(self,-1)

        self.r1 = wx.RadioButton(self.panel,-1,"Elmo",pos=(20,50),style=wx.RB_GROUP)
        self.r2 = wx.RadioButton(self.panel,-1,"Ernie",pos=(20,80))
        self.r3 = wx.RadioButton(self.panel,-1,"Bert",pos=(20,110))

        self.t1 = wx.TextCtrl(self.panel,-1,"",pos=(80,50))
        self.t2 = wx.TextCtrl(self.panel,-1,"",pos=(80,80))
        self.t3 = wx.TextCtrl(self.panel,-1,"",pos=(80,110))
        
        self.texts = {'Elmo':self.t1,'Ernie':self.t2,'Bert':self.t3}

        for eachText in [self.t2,self.t3]:
            eachText.Enable(False)
        for eachRadio in [self.r1,self.r2,self.r3]:
            self.Bind(wx.EVT_RADIOBUTTON,self.OnRadio,eachRadio)
        self.selectedText = self.t1

    def OnRadio(self,event):
        if self.selectedText:
            print(self.selectedText)
            self.selectedText.Enable(False)
        radioSelected = event.GetEventObject()
        text = self.texts[radioSelected.GetLabel()]
        text.Enable(True)
        self.selectedText = text

class App(wx.App):
    def OnInit(self):
        self.frame = RadioButtonFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
