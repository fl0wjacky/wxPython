#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''创建自定义事件的步骤：
    1.定义一个新的事件类，它是wxPython的wx.PyEvent类的子类。如果你想这个事件被作为命令事件，你可以创建wx.PyCommandEvent的子类，像许多wxPython中的覆盖一样，一个类的py版本使得wxWidgt系统明白用Python写的版本覆盖C++版本。
    2.创建一个事件类型和一个绑定器对象去绑定该事件到特定的对象。
    3.添加能够建造这个新事件实例的代码，并且使用ProcessEvent()方法将这个实例引入事件处理系统。一旦该事件被创建，你就可以像使用其他的wxPython事件一样创建绑定和处理方法。'''
import wx

class TwoButtonEvent(wx.PyCommandEvent):    #定义事件
    def __init__(self,evtType,id):
        wx.PyCommandEvent.__init__(self,evtType,id)
        self.clickCount = 0
    def GetClickCount(self):
        return self.clickCount
    def SetClickCount(self,count):
        self.clickCount=count

myEVT_TWO_BUTTON=wx.NewEventType()  #创建一个事件类型
EVT_TWO_BUTTON=wx.PyEventBinder(myEVT_TWO_BUTTON,1) #创建一个事件绑定器

class TwoButtonPanel(wx.Panel):
    def __init__(self,parent,id=-1,leftText="Left",rightText="Right"):
        wx.Panel.__init__(self,parent,id)
        self.leftButton=wx.Button(self,label=leftText,pos=(10,20),size=(50,30))
        self.rightButton=wx.Button(self,label=rightText,pos=(10,50),size=(50,30))
        self.leftClick = False
        self.rightClick = False
        self.clickCount=0
        self.rightButton.Bind(wx.EVT_LEFT_DOWN,self.OnRightClick)
        self.leftButton.Bind(wx.EVT_LEFT_DOWN,self.OnLeftClick)
    def OnLeftClick(self,event):
        self.leftClick=True
        self.OnClick()
        event.Skip()
    def OnRightClick(self,event):
        self.rightClick=True
        self.OnClick()
        event.Skip()
    def OnClick(self):
        self.clickCount+=1
        if self.rightClick and self.leftClick:
            self.rightClick = False
            self.leftClick = False
            evt=TwoButtonEvent(myEVT_TWO_BUTTON,self.GetId())#创建自定义事件
            evt.SetClickCount(self.clickCount)#添加数据到事件
            self.GetEventHandler().ProcessEvent(evt)#处理事件

class CustomEventFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Click Count:0",size=(300,100))
        self.panel = TwoButtonPanel(self)
        self.Bind(EVT_TWO_BUTTON,self.OnTwoClick,self.panel)#绑定事件
    def OnTwoClick(self,event):#定义一个事件处理器
        self.SetTitle("Click Count:%s" % event.GetClickCount())

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = CustomEventFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()
