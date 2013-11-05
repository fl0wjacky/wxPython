#! /usr/bin/env python
# coding:utf-8

import wx
import os

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    dialog = wx.DirDialog(None,
        style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    dialog.SetPath('/tmp')
    if dialog.ShowModal() == wx.ID_OK:
        print dialog.GetPath()

    dialog.Destroy()
    
    #函数
    print(wx.DirSelector('Choose Me'))
