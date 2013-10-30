#! /usr/bin/env python
# -*- coding:utf-8 -*-

import wx
from ch06_SketchWindow import SketchWindow
class SketchFrame(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,-1,"Sketch Frame",size=(800,600))
        self.sketch = SketchWindow(self,-1)
        self.sketch.Bind(wx.EVT_MOTION,self.OnSketchMotion)
        self.initStatusBar()#1这里因重构有点变化
        self.createMenuBar()

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def OnSketchMotion(self,event):
        self.statusbar.SetStatusText("Pos:%s" % str(event.GetPositionTuple()),0)
        self.statusbar.SetStatusText("Current Pts:%s" % len(self.sketch.curLine),1)
        self.statusbar.SetStatusText("Line Count:%s" % len(self.sketch.lines),2)
        event.Skip()

    def menuData(self):#2菜单数据
        return [("&File",(
                ("&New","New Sketch file",self.OnNew),
                ("&Open","Open sketch file",self.OnOpen),
                ("&Save","Save sketch file",self.OnSave),
                ("","",""),
                ("&Color",(
                    ("&Black","",self.OnColor,wx.ITEM_RADIO),
                    ("&Red","",self.OnColor,wx.ITEM_RADIO),
                    ("&Green","",self.OnColor,wx.ITEM_RADIO),
                    ("&Blue","",self.OnColor,wx.ITEM_RADIO))),
                ("","",""),
                ("&Quit","Quit",self.OnCloseWindow)))]

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems),menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self,menuData):
        menu = wx.Menu()
    #3创建子菜单
        for eachItem in menuData:
            if len(eachItem) == 2:
               label = eachItem[0]
               subMenu = self.createMenu(eachItem[1])
               menu.AppendMenu(wx.NewId(),label,subMenu)
            else:
                self.createMenuItem(menu,*eachItem)
        return menu

    def createMenuItem(self,menu,label,status,handler,kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1,label,status,kind)#4使用kind创建菜单项
        self.Bind(wx.EVT_MENU,handler,menuItem)

    def OnNew(self,event):pass
    def OnOpen(self,event):pass
    def OnSave(self,event):pass

    def OnColor(self,event):#5处理颜色的变化
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnCloseWindow(self,event):
        self.Destroy()

class App(wx.App):
    def OnInit(self):
        self.frame = SketchFrame(None)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
