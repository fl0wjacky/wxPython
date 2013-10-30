#! /usr/bin/env python
# condig:utf-8

import wx
import wx.lib.buttons as buttons

class GenericButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Generic Button Example",
            size=(600,350))
        self.panel = wx.Panel(self,-1)

        sizer = wx.FlexGridSizer(1,3,20,20)
        b = wx.Button(self.panel,-1,"A wx.Button")
        b.SetDefault()
        sizer.Add(b)

        b = wx.Button(self.panel,-1,'non-default wx.Button')
        sizer.Add(b)
        sizer.Add((10,10))

        b = buttons.GenButton(self.panel,-1,'Generic Button')
        sizer.Add(b)
        
        b = buttons.GenButton(self.panel,-1,'disabled Generic')
        b.Enable(False)
        sizer.Add(b)

        b = buttons.GenButton(self.panel,-1,'bigger')
        b.SetFont(wx.Font(20,wx.SWISS,wx.NORMAL,wx.BOLD,False))
        b.SetBezelWidth(5)
        b.SetBackgroundColour('Navy')
        b.SetForegroundColour('white')
        b.SetToolTipString("This is a BIG button...")
        sizer.Add(b)

        bmp = wx.Image('car.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        b = buttons.GenBitmapButton(self.panel,-1,bmp)
        sizer.Add(b)

        self.b = buttons.GenBitmapToggleButton(self.panel,-1,bmp)
        sizer.Add(self.b)
        
        b = buttons.GenBitmapTextButton(self.panel,-1,bmp,
            'Bitmapped Text',size=(175,75))
        b.SetUseFocusIndicator(False)
        sizer.Add(b)

        self.tb = buttons.GenToggleButton(self.panel,-1,'Toggle Button')
        sizer.Add(self.tb)

        self.panel.SetSizer(sizer)

class App(wx.App):
    def OnInit(self):
        self.frame = GenericButtonFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
