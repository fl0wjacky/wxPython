#! /usr/bin/env python 
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    choices = ['Alpha','Beker','Charlie','Delta']
    dialog = wx.SingleChoiceDialog(None,'Pick A Work','Choices',choices)
    dialog.SetSelection(1)
    if dialog.ShowModal() == wx.ID_OK:
        print 'You selected: %s\n' % dialog.GetStringSelection()

    dialog.Destroy()

    # 函数 两类：一个返回所选字符串，一个返回索引值
    ret = []
    ret.append(wx.GetSingleChoice('Pick A Work','Choices',choices))
    ret.append(wx.GetSingleChoiceIndex('Pick A Work','Choices',choices))
    print(ret)
