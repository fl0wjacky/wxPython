#! /usr/bin/env python
# coding:utf-8

import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Text Entry Example',size=(300,250))
        self.panel = wx.Panel(self,-1)
        self.multiLabel = wx.StaticText(self.panel,-1,"Multi-line")
        self.multiText = wx.TextCtrl(self.panel,-1,
            "Here is a looooooooooong line of text set in the control.\n\n"
            "See that it wrapped, and that this line is after a blank",
            size=(200,100),style=wx.TE_MULTILINE)#创建一个文本控件
        self.multiText.SetInsertionPoint(0)#设置插入点

        self.richLabel = wx.StaticText(self.panel,-1,"Rich Text")
        self.richText = wx.TextCtrl(self.panel,-1,
            "If supported by the native control, this is reversed,and this"
            " is a different font.",
            size=(200,100),style=wx.TE_MULTILINE | wx.TE_RICH2)#创建丰富文本控件
        self.richText.SetInsertionPoint(0)
        self.richText.SetStyle(44,52,wx.TextAttr("white","black"))
        points = self.richText.GetFont().GetPointSize()
        f = wx.Font(points+3,wx.ROMAN,wx.ITALIC,wx.BOLD,True)
        self.richText.SetStyle(67,82,wx.TextAttr('blue',wx.NullColour,f))
        
        sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        sizer.AddMany([self.multiLabel,self.multiText,
            self.richLabel,self.richText])
        self.panel.SetSizer(sizer)

class App(wx.App):
    def OnInit(self):
        self.frame = TextFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
