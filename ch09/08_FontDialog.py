#! /usr/bin/env python
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    dialog = wx.FontDialog(None, wx.FontData())
    if dialog.ShowModal() == wx.ID_OK:
        data = dialog.GetFontData()
        font = data.GetChosenFont()
        colour = data.GetColour()
        print "You selected:'%s', %d points\n" % (font.GetFaceName(),font.GetPointSize())

    #dialog.Destroy()

    # 函数
        #font = wx.Font()
        newFont = wx.GetFontFromUser(None,font)
        print(newFont.Ok())

    dialog.Destroy() 
