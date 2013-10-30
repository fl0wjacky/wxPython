#! /usr/bin/env python
# coding:utf-8

import wx
from wx.lib.stattext import GenStaticText as GST

class StaticTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Static Text Example',size=(400,300))
        self.panel = wx.Panel(self,-1)

        self.one = GST(self.panel,wx.NewId(),"This is an example of static text",
            (100,10))

        self.rev = GST(self.panel,wx.NewId(),"Static Text With Reversed Colors",(100,30))
        self.rev.SetForegroundColour('white')
        self.rev.SetBackgroundColour('black')

        self.center = GST(self.panel,wx.NewId(),"align center",(100,50),
            (160,-1),wx.ALIGN_CENTER)
        self.center.SetForegroundColour('white')
        self.center.SetBackgroundColour('black')

        self.right = GST(self.panel,wx.NewId(),"align right",(100,70),
            (160,-1),wx.ALIGN_RIGHT)
        self.right.SetForegroundColour('white')
        self.right.SetBackgroundColour('black')
      
        str = "You can also change the font."
        self.text = GST(self.panel,wx.NewId(),str,(20,100))
        font = wx.Font(18,wx.DECORATIVE,wx.ITALIC,wx.NORMAL)
        self.text.SetFont(font)
 
        GST(self.panel,wx.NewId(),"Your text\ncan be split\n"
            "over multiple lines\n\neven blank ones",(20,150))
        GST(self.panel,wx.NewId(),"Multi-line text\ncan also\n"
            "be right aligned\n\neven with a blank",(220,150),
            style=wx.ALIGN_RIGHT)
class App(wx.App):
    def OnInit(self):
        self.frame = StaticTextFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
