#! /usr/bin/env python
# -*- coding:utf-8 -*-
import wx
import wx.grid

class LineupEntry:
    def __init__(self,pos,first,last):
        self.pos = pos
        self.first = first
        self.last = last

class LineupTable(wx.grid.PyGridTableBase):
    colLabels = ("First","Last")        #列标签
    cloAttrs = ("first","last")         #1属性名
    def __init__(self,entries):         #2初始化模型
        wx.grid.PyGridTableBase.__init_(self)
        self.entries = entries
    def GetNumberRows(self):
        return len(self.entries)
    def GetNumberCols(self):
        return 2
    def GetColLabelValue(self,col):
        return self.colLabels[col]      #读列标签
    def GetRowLabelValue(self,row):
        return self.entries[row].pos    #3读行标签
    def IsEmptyCell(self,row,col):
        return False
    def GetValue(self,row,col):
        entry = self.entries[row]
        return getattr(entry,self.colAttrs[col])#4读属性值
    def SetValue(self,row,col,value):
        pass
