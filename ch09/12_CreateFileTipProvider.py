#! /usr/bin/env python
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    provider = wx.CreateFileTipProvider("tips.txt",0)
    wx.ShowTip(None,provider,True)
