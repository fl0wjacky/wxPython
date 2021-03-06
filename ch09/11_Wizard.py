#! /usr/bin/env python
# coding:utf-8

import wx
import wx.wizard

class TitledPage(wx.wizard.WizardPageSimple): # 1 创建页面样板
    def __init__(self,parent,title):
        wx.wizard.WizardPageSimple.__init__(self,parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        titleText = wx.StaticText(self,-1,title)
        titleText.SetFont(
            wx.Font(18,wx.SWISS,wx.NORMAL,wx.BOLD))
        self.sizer.Add(titleText,0,wx.ALIGN_CENTER | wx.ALL,5)
        self.sizer.Add(wx.StaticLine(self,-1),0,wx.EXPAND | wx.ALL,5)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    app.MainLoop()

    wizard = wx.wizard.Wizard(None, -1, "Simple Wizard") # 创建向导实例

    #创建向导页面
    page1 = TitledPage(wizard,"Page 1")
    page2 = TitledPage(wizard,"Page 2")
    page3 = TitledPage(wizard,"Page 3")
    page4 = TitledPage(wizard,"Page 4")

    page1.sizer.Add(wx.StaticText(page1,-1,"Testing the wizard"))
    page4.sizer.Add(wx.StaticText(page4,-1,"This is the last page."))

    # 2 创建页面链接
    wx.wizard.WizardPageSimple_Chain(page1,page2)
    wx.wizard.WizardPageSimple_Chain(page2,page3)
    wx.wizard.WizardPageSimple_Chain(page3,page4)

    wizard.FitToPage(page1) # 3 调整向导的尺寸

    if wizard.RunWizard(page1): # 4 运行向导
        print "Success"

    wizard.Destroy()
