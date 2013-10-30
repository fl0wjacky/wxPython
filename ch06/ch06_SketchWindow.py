#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ？为什么不捕获鼠标的时候窗口变化的时候之前画的线条就完全消失了
import wx
class SketchWindow(wx.Window):
    def __init__(self,parent,ID):
        wx.Window.__init__(self,parent,ID)
        self.SetBackgroundColour("White")
        self.color = "Black"
        self.thickness = 1
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)#1创建一个wx.Pen对象
        self.lines = []
        self.curLine = []
        self.pos = (0,0)
        self.InitBuffer()
        #2连接事件
        self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,self.OnMotion)
        self.Bind(wx.EVT_SIZE,self.OnSize)
        self.Bind(wx.EVT_IDLE,self.OnIdle)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
    def InitBuffer(self):
        size = self.GetClientSize()
    #3创建一个缓存的设备上下文
        self.buffer = wx.EmptyBitmap(size.width,size.height)
        dc = wx.BufferedDC(None,self.buffer)
    #4使用设备上下文
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)
        
        self.reInitBuffer = False
    
    def GetLinesData(self):
        return self.lines[:]

    def SetLinesData(self,lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()

    def OnLeftDown(self,event):
        self.curLine = []
        self.pos = event.GetPositionTuple()#5得到鼠标的位置
        self.CaptureMouse()#6捕获鼠标

    def OnLeftUp(self,event):
        if self.HasCapture():
            self.lines.append((self.color,self.thickness,self.curLine))
            self.curLine = []
            self.ReleaseMouse()#7释放鼠标

    def OnMotion(self,event):
        if event.Dragging() and event.LeftIsDown():#8确定是否在拖动
            dc = wx.BufferedDC(wx.ClientDC(self),self.buffer)#9创建另一个缓存的上下文
            self.drawMotion(dc,event)
            event.Skip()
    #10绘画到设备上下文
    def drawMotion(self,dc,event):
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos
    def OnSize(self,event):
        self.reInitBuffer = True    #11处理一个resize事件
    def OnIdle(self,event): #12空闲时的处理
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)
    def OnPaint(self,event):
        dc = wx.BufferedPaintDC(self,self.buffer)#13处理一个paint(描绘)请求
    #14绘制所有得线条
    def DrawLines(self,dc):
        for color,thickness,line in self.lines:
            pen = wx.Pen(color,thickness,wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)
    def SetColor(self,color):
        self.color = color
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)
    def SetThickness(self,num):
        self.thickness = num
        self.pen = wx.Pen(self.color,self.thickness,wx.SOLID)

class SketchFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"Sketch Frame",size=(800,600))
        self.sketch = SketchWindow(self,-1)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()
