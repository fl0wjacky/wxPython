#! /usr/bin/env python
# coding:utf-8

import wx
import os

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    wildcard = "Python source(*.py)|*.py|Complied Python(*.pyc)|*.pyc|All files(*.*)|*.*"
    dialog = wx.FileDialog(None,"Choose a file",os.getcwd(),'',wildcard,wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        print dialog.GetPath()

    dialog.Destroy()
    
    #函数 如果用户按下OK，返回值是字符串形式的路径名，如果用户按下Cancel则返回一个空字符串
    print(wx.FileSelector("Pick One",os.getcwd(),'','.py','python|*.py|All|*.*',wx.SAVE))
