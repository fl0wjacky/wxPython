#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''错误总结：对于只有一个元素的元组，需要在右括号前加上一个逗号：
    如：menu = ("About",(("&About","",self.OnAbout),))'''
import wx
import os
import pickle
from ch06_ControlPanel import ControlPanel
from ch06_SketchWindow import SketchWindow
from ch06_SketchAbout import SketchAbout

class SketchFrame(wx.Frame):
    def __init__(self,parent):
        self.title = "Sketch Frame"
        wx.Frame.__init__(self,parent,-1,self.title,size=(800,600))
        self.filename = ''
        self.wildcard = "Sketch file(*.sketch)|*.sketch|All files(*.*)|*.*"
        self.sketch = SketchWindow(self,-1)
        self.sketch.Bind(wx.EVT_MOTION,self.OnSketchMotion)
        self.initStatusBar()
        self.createMenuBar()
        self.createPanel()

    def createPanel(self):
        controlPanel = ControlPanel(self,-1,self.sketch)
        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(controlPanel,0,wx.EXPAND)
        box.Add(self.sketch,1,wx.EXPAND)
        self.SetSizer(box)


    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def OnSketchMotion(self,event):
        self.statusbar.SetStatusText("Pos:%s" % str(event.GetPositionTuple()),0)
        self.statusbar.SetStatusText("Current Pts:%s" % len(self.sketch.curLine),1)
        self.statusbar.SetStatusText("Line Count:%s" % len(self.sketch.lines),2)
        event.Skip()

    def menuData(self):
        return [("&File",(
                ("&New","New Sketch file",self.OnNew),
                ("&Open","Open sketch file",self.OnOpen),
                ("&Save","Save sketch file",self.OnSave),
                ("","",""),
                ("&Color",(
                    ("&Black","",self.OnColor,wx.ITEM_RADIO),
                    ("&Red","",self.OnColor,wx.ITEM_RADIO),
                    ("&Green","",self.OnColor,wx.ITEM_RADIO),
                    ("&Blue","",self.OnColor,wx.ITEM_RADIO),
                    ("&Other...","",self.OnOtherColor))),
                ("","",""),
                ("&Quit","Quit",self.OnCloseWindow))),
                ("About",(
                ("&About",'',self.OnAbout),))]

    def OnAbout(self,event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems),menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self,menuData):
        menu = wx.Menu()
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
        menuItem = menu.Append(-1,label,status,kind)
        self.Bind(wx.EVT_MENU,handler,menuItem)

    def OnNew(self,event):pass

    def OnColor(self,event):
        menubar = self.GetMenuBar()
        itemId = event.GetId()
        item = menubar.FindItemById(itemId)
        color = item.GetLabel()
        self.sketch.SetColor(color)

    def OnCloseWindow(self,event):
        self.Destroy()

    def SaveFile(self):#1保存文件
        if self.filename:
            data = self.sketch.GetLinesData()
            with open(self.filename,'wb') as f:
                pickle.dump(data,f)

    def ReadFile(self):#2读文件
        if self.filename:
            try:
                f = open(self.filename,'rb')
                data = pickle.load(f)
                f.close()
                self.sketch.SetLinesData(data)
            except EOFError:
                wx.MessageBox("%s is not a sketch file." % self.filename,"oops!",style = wx.OK|wx.ICON_EXCLAMATION)

    def OnOpen(self,event):
        dlg = wx.FileDialog(self,"Open sketch file...",
            os.getcwd(),style = wx.OPEN, wildcard = self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            print('You perss button [OK]')
            self.filename = dlg.GetPath()
            print('You get the filename %s' % self.filename)
            self.ReadFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()

    def OnSave(self,event):#4保存文件
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveFile()

    def OnSaveAs(self,event):#5弹出保存对话框
        dlg = wx.FileDialog(self,"Save sketch as...",
            os.getcwd(),style=wx.SAVE|wx.OVERWRITE_PROMPT,
            wildcard = self.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename)[1]:#6确保文件名后缀
                filename = filename + '.sketch'
            self.filename = filename
            self.SaveFile()
            self.SetTitle(self.title + '--' + self.filename)
        dlg.Destroy()

    def OnOtherColor(self,event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)#创建颜色数据对象
        if dlg.ShowModal() == wx.ID_OK:
            self.sketch.SetColor(dlg.GetColourData().GetColour())#根据用户的输入设置颜色
        dlg.Destroy()
    
    def MakeBitmap(self,color):
        bmp = wx.EmptyBitmap(16,15)
        dc = wx.MemoryDC()
        dc.SelectObject(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp

class App(wx.App):
    def OnInit(self):
        self.frame = SketchFrame(None)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
