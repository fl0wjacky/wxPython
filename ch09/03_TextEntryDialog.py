#! /usr/bin/env python 
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    dialog = wx.TextEntryDialog(None,
        "What kind of text would you like to enter?","Text Entry","Default Value",style = wx.OK | wx.CANCEL | wx.TE_PASSWORD | wx.TE_CENTER)
    retCode = dialog.ShowModal()
    if retCode == wx.ID_OK:
        print "You entered:%s" % dialog.GetValue()
    elif retCode == wx.ID_CANCEL:
        print "you cancel the option."

    dialog.Destroy()
    
    # 方法二 三类函数
    message = "Hey,What I can do for you?"
    ret = []
    ret.append(wx.GetTextFromUser(message))
    ret.append(wx.GetPasswordFromUser(message))
    ret.append(wx.GetNumberFromUser(message,"-100 to 100","Input A Number",10,-100,100))
    print(ret)
