#! /usr/bin/env python
# coding:utf-8

import wx
import random
random.seed()

class RandomImagePlacementWindow(wx.Window):
    def __init__(self, parent, image):
        wx.Window.__init__(self, parent)
        self.photo = image.ConvertToBitmap() # Create the bitmap

        # choose some random positions to draw the image at:
        self.positions = [(10,10)]
        for x in range(5):
            x = random.randint(0,600)
            y = random.randint(0,400)
            self.positions.append((x,y))

        #Bind the Paint event
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, evt):
        # create and  clear the DC
        dc = wx.PaintDC(self)
        brush = wx.Brush('sky blue')
        dc.SetBackground(brush)
        dc.Clear()

        for x, y in self.positions:
            dc.DrawBitmap(self.photo, x, y, True)
            dc.DrawIcon(wx.Icon('smiles.ico', wx.BITMAP_TYPE_ICO), x+70, y+70)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = 'Loading Images', size = (640, 480))
        img = wx.Image('masked-portrait.png')
        win = RandomImagePlacementWindow(self, img)

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
