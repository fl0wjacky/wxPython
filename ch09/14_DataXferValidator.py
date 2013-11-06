#! /usr/bin/env python
# coding:utf-8

import wx
import pprint

about_txt = '''\
The validator used in this example will ensure that the text 
controls are not empty when you press the Ok button,and 
will not let you leave if any of the Validations fail.'''

class DataXferValidator(wx.PyValidator): # 声明验证器
    def __init__(self,data,key):
        wx.PyValidator.__init__(self)
        self.data = data
        self.key = key

    def Clone(self):
        '''Note that every validator must implement the Clone() method.'''
        return DataXferValidator(self.data,self.key)

    def Validate(self,win): # 没有验证数据
        return True

    def TransferToWindow(self): # 对话框打开时被调用
        textCtrl = self.GetWindow()
        textCtrl.SetValue(self.data.get(self.key,''))
        return True

    def TransferFromWindow(self): # 对话框关闭时被调用
        textCtrl = self.GetWindow()
        self.data[self.key] = textCtrl.GetValue()
        return True

class MyDialog(wx.Dialog):
    def __init__(self,data):
        wx.Dialog.__init__(self,None,-1,"Validators: data transfer")

        #Create the text controls
        about = wx.StaticText(self,-1,about_txt)
        name_l = wx.StaticText(self,-1,"Name:")
        email_l = wx.StaticText(self,-1,"Email:")
        phone_l = wx.StaticText(self,-1,"Phone:")

        # 2 将验证器与窗口部件相关联
        name_t = wx.TextCtrl(self,validator=DataXferValidator(data,"name"))
        email_t = wx.TextCtrl(self,validator=DataXferValidator(data,'email'))
        phone_t = wx.TextCtrl(self,validator=DataXferValidator(data,'phone'))

        # Use standard button IDs
        okey = wx.Button(self,wx.ID_OK)
        okey.SetDefault()
        cancel = wx.Button(self,wx.ID_CANCEL)

        # Layout with sizers
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(about,0,wx.ALL,5)
        sizer.Add(wx.StaticLine(self),0,wx.EXPAND | wx.ALL, 5)

        fgs = wx.FlexGridSizer(3,2,5,5)
        fgs.Add(name_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(name_t, 0, wx.EXPAND)
        fgs.Add(email_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(email_t, 0, wx.EXPAND)
        fgs.Add(phone_l, 0, wx.ALIGN_RIGHT)
        fgs.Add(phone_t, 0, wx.EXPAND)
        fgs.AddGrowableCol(1)
        sizer.Add(fgs, 0, wx.EXPAND | wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(okey)
        btns.AddButton(cancel)
        btns.Realize()
        sizer.Add(btns, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

if __name__ == "__main__":
    app = wx.PySimpleApp()

    data = {'name':'fl0wjacky','email':'flowjacky@gmail.com','phone':'186****9654'}
    dlg = MyDialog(data)
    dlg.ShowModal()
    dlg.Destroy()

    wx.MessageBox("You entered these values:\n\n" + pprint.pformat(data))
    app.MainLoop()
