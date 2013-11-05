#! /usr/bin/env python
# coding:utf-8

'''
if the button ID is wx.ID_OK or wx.ID_CANCEL or the integers these two button present,the behaviours are pre-defined,
else you have to define the handler method by yourself
'''

import wx

class SubclassDialog(wx.Dialog):
    def __init__(self): # 初始化对话框
        wx.Dialog.__init__(self,None,-1,"Dialog Subclass",size=(300,100))
        okButton = wx.Button(self,wx.ID_OK,"OK",pos = (15,15))
        okButton.SetDefault()
        cancelButton = wx.Button(self,wx.ID_CANCEL,"Cancel",pos = (115,15))

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()
    dialog = SubclassDialog()
    result = dialog.ShowModal() # 显示模式对话框
    if result == wx.ID_OK:
        print "OK"
    else:
        print "Cancel"
    dialog.Destroy()
