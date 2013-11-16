#! /usr/bin/env python
# coding:utf-8

import wx

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Real World Test')
        self.panel = panel = wx.Panel(self)

        #First create the controls
        topLbl = wx.StaticText(panel, -1, 'Account Information')
        topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))

        nameLbl = wx.StaticText(panel, -1, 'Name:')
        name = wx.TextCtrl(panel, -1, '')

        addrLbl = wx.StaticText(panel, -1, 'Address:')
        addr1 = wx.TextCtrl(panel, -1, '')
        addr2 = wx.TextCtrl(panel, -1, '')

        cstLbl = wx.StaticText(panel, -1, 'City State, Zip:')
        city = wx.TextCtrl(panel, -1, '', size = (150, -1))
        state = wx.TextCtrl(panel, -1, '', size = (50, -1))
        zip = wx.TextCtrl(panel, -1, '', size = (70, -1))

        phoneLbl = wx.StaticText(panel, -1, 'Phone:')
        phone = wx.TextCtrl(panel, -1, '')

        emailLbl = wx.StaticText(panel, -1, 'Email:')
        email = wx.TextCtrl(panel, -1, '')

        saveBtn = wx.Button(panel, -1, 'Save')
        cancelBtn = wx.Button(panel, -1, 'Cancel')

        #Now do the layout.
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(topLbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

        addrSizer = wx.FlexGridSizer(cols = 2, hgap = 5, vgap = 5)
        addrSizer.AddGrowableCol(1)
        addrSizer.Add(nameLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(name, 0, wx.EXPAND)
        addrSizer.Add(addrLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(addr1, 0, wx.EXPAND)
        addrSizer.Add((10, 10))
        addrSizer.Add(addr2, 0, wx.EXPAND)
        addrSizer.Add(cstLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        cstSizer = wx.BoxSizer(wx.HORIZONTAL)
        cstSizer.Add(city, 1)
        cstSizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        cstSizer.Add(zip)
        addrSizer.Add(cstSizer, 0, wx.EXPAND)
        
        addrSizer.Add(phoneLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(phone, 0, wx.EXPAND)
        addrSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        addrSizer.Add(email, 0, wx.EXPAND)

        mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(saveBtn)
        btnSizer.Add((20, 20), 1)
        btnSizer.Add(cancelBtn)
        btnSizer.Add((20, 20), 1)

        mainSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)

        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        mainSizer.SetSizeHints(self)

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
