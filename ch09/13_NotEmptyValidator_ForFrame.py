#! /usr/bin/env python
# coding:utf-8

import wx

class NotEmptyValidator(wx.PyValidator):
    def __init__(self,data,key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key

    def Clone(self):
        return NotEmptyValidator(self.data,self.key)

    def Validate(self,win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()

        if len(text) == 0:
            wx.MessageBox("This field must contain some text!","Error")
            textCtrl.SetBackgroundColour('pink')
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        TextCtrl = self.GetWindow()
        TextCtrl.SetValue(self.data.get(self.key,''))
        return True

    def TransferFromWindow(self):
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

class MyFrame(wx.Frame):
    def __init__(self,data):
        self.data = data
        wx.Frame.__init__(self,None,-1,'Validator Frame',size=(400,300),style=wx.DEFAULT_FRAME_STYLE)
        self.panel = wx.Panel(self,-1)
        self.tc1 = wx.TextCtrl(self.panel,-1,validator=NotEmptyValidator(self.data,'name'),pos=(10,10))
        self.tc2 = wx.TextCtrl(self.panel,-1,validator=NotEmptyValidator(self.data,'age'),pos=(100,10))
        self.button = wx.Button(self.panel,-1,"Validate",pos=(50,100))

        self.Bind(wx.EVT_BUTTON,self.ValidateClose,self.button)
        self.tc1.GetValidator().TransferToWindow()
        self.tc2.GetValidator().TransferToWindow()

    def ValidateClose(self,evt):
        v1 = self.tc1.GetValidator()
        v2 = self.tc2.GetValidator()
        if v1.Validate(self.tc1) and v2.Validate(self.tc2):
            self.Close()

class App(wx.App):
    def OnInit(self):
        data = {'name':'fl0w','age':'23'}
        self.frame = MyFrame(data)
        self.frame.Show()
        return True
if __name__ == "__main__":
    app = App()
    app.MainLoop()
