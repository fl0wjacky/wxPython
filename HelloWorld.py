#! /usr/bin/env python 
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    wx.Frame(None,-1,'hello world!').Show(True)
    app.MainLoop()
