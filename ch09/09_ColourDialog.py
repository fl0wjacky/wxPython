#! /usr/bin/env python
# coding:utf-8

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    dialog = wx.ColourDialog(None)
    dialog.GetColourData().SetChooseFull(True)
    if dialog.ShowModal() == wx.ID_OK:
        data = dialog.GetColourData()
        print "You selected: %s\n" % str(data.GetColour().Get())

    dialog.Destroy()

    # 函数
    c = wx.Colour(255,255,255)
    retC = wx.GetColourFromUser(None,c)
    print(retC.Ok())

'''
wx.ColourData.SetChooseFull(self,int flag)
    Under Windows, tells the Windows colour dialog to display the full dialog with custom colour controls.
    Under other platforms, has no effect. The default value is true.
'''
