#! /usr/bin/env python
# coding:utf-8

import wx

filenames = ['image.bmp', 'image.gif', 'image.jpg', 'image.png']
class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Loading Images')
        self.panel = p = wx.Panel(self)
        
        wx.SetCursor(wx.Cursor('smiles.ico',wx.BITMAP_TYPE_ICO))

        fgs = wx.FlexGridSizer(cols = 2, hgap = 10, vgap = 10)
        
        for file in filenames:
            img1 = wx.Image(file, wx.BITMAP_TYPE_ANY)

            w = img1.GetWidth()
            h = img1.GetHeight()

            img2 = img1.Scale(w/2, h/2)

            sb1 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img1))
            sb2 = wx.StaticBitmap(p, -1, wx.BitmapFromImage(img2))

            fgs.Add(sb1)
            fgs.Add(sb2)

        p.SetSizer(fgs)
        fgs.SetSizeHints(self)
        self.Fit()
        
class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == '__main__':
    App().MainLoop()
