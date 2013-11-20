#! /usr/bin/env python 
# coding:utf-8

'''记住根据图片的情况设置掩码'''

import wx

class MoveFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Move Frame',style=wx.FRAME_SHAPED | wx.SIMPLE_BORDER)
        img = wx.Image('trans.png',wx.BITMAP_TYPE_PNG)
        
        #1 下面5行为手动设置图片掩码的第一种方法
        if not img.HasMask():
            img.SetMaskColour(255,255,255)
        else:
            print('Yes,I have a Image musk')
        img.SetMask(True)

        self.bmp = wx.BitmapFromImage(img)

        #2 下面三行为手动设置图片掩码的第二种方法
        '''print(self.bmp.GetMask())
        if not  self.bmp.GetMask():
            self.bmp.SetMask(wx.Mask(self.bmp,wx.WHITE))'''

        self.SetClientSize((self.bmp.GetWidth(),self.bmp.GetHeight()))
        self.delta = wx.Point(0,0)

        self.Bind(wx.EVT_WINDOW_CREATE,self.SetWindowShape)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,self.OnMove)
        self.Bind(wx.EVT_RIGHT_UP,self.OnExit)

    def SetWindowShape(self,evt=None):
        r = wx.RegionFromBitmap(self.bmp)
        self.SetShape(r)

    def OnPaint(self,evt):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bmp,0,0,True)

    def OnLeftDown(self,evt):
        self.CaptureMouse()
        pos = self.ClientToScreen(evt.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)
        #print('Rigth Button')按下时触发一次，移动的过程中不会触发

    def OnLeftUp(self,evt):
        if self.HasCapture():
            self.ReleaseMouse()

    def OnMove(self,evt):
        if evt.Dragging() and evt.LeftIsDown():
            pos = self.ClientToScreen(evt.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)

    def OnExit(self,evt):
        self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MoveFrame()
    frame.Show(True)
    app.MainLoop()
