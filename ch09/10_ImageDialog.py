#! /usr/bin/env python
# coding:utf-8

import wx
from wx.lib.imagebrowser import ImageDialog

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    dialog = ImageDialog(None)
    if dialog.ShowModal() == wx.ID_OK:
        print "You Selected File: " + dialog.GetFile()

    dialog.Destroy()
