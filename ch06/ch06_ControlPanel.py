#! /usr/bin/env python
# coding:utf-8

import wx
import wx.lib.buttons
class ControlPanel(wx.Panel):
    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4

    colorList = ('Black','Yellow','Red','Green','Blue','Purple',
                'Brown','Aquamarine','Forest Green','Light Blue',
                'Goldenrod','Cyan','Orange','Navy','Dark Grey',
                'Light Grey')
    maxThickness = 16

    def __init__(self,parent,ID,sketch):
        wx.Panel.__init__(self,parent,ID,style=wx.RAISED_BORDER)
        self.sketch = sketch
        buttonSize = (self.BMP_SIZE + 2*self.BMP_BORDER,
            self.BMP_SIZE + 2*self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent,buttonSize)
        thicknessGrid = self.createThicknessGrid(buttonSize)
        self.layout(colorGrid,thicknessGrid)

    def createColorGrid(self,parent,buttonSize):#1 创建颜色网格
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(cols = self.NUM_COLS,hgap=2,vgap=2)
        for eachColor in self.colorList:
            bmp = parent.MakeBitmap(eachColor)
            b = wx.lib.buttons.GenBitmapToggleButton(self,-1,bmp,size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON,self.OnSetColour,b)
            colorGrid.Add(b,0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid
    
    def createThicknessGrid(self,buttonSize): #2 创建线条粗细网格
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols = self.NUM_COLS,hgap = 2,vgap = 2)
        for x in range(1,self.maxThickness+1):
            b = wx.lib.buttons.GenToggleButton(self,-1,str(x),size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON,self.OnSetThickness,b)
            thicknessGrid.Add(b,0)
            self.thicknessIdMap[b.GetId()] = x
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def layout(self,colorGrid,thicknessGrid):# 3合并网格
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(colorGrid,0,wx.ALL,self.SPACING)
        box.Add(thicknessGrid,0,wx.ALL,self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def OnSetColour(self,event):
        color = self.colorMap[event.GetId()]
        if color != self.sketch.color:
            self.colorButtons[self.sketch.color].SetToggle(False)
        self.sketch.SetColor(color)

    def OnSetThickness(self,event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.sketch.thickness:
            self.thicknessButtons[self.sketch.thickness].SetToggle(False)
        self.sketch.SetThickness(thickness)
