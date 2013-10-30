#! /usr/bin/env python
# -*- coding:utf-8 -*-
import wx

class RefactorFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title = "重构",size = (340,200))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("White")
        self.createMenuBar()
        self.createButtonBar(self.panel)
        self.createTextFields(self.panel)
    
    def menuData(self):
        return (("&File",("&Open","Open",self.OnOpen),
                            ("&Quit","Quit",self.OnQuit)),
                ("&Edit",("&Copy","Copy",self.OnCopy),
                            ("C&ut","Cut",self.OnCut),
                            ("&Paste","Paste",self.OnPaste),
                            ("","",None),
                            ("&Options...","Options",self.OnOptions)))
    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for item in self.menuData():
            menuLabel = item[0]
            menuItem = item[1:]
            menuBar.Append(self.createMenu(menuItem),menuLabel)
        self.SetMenuBar(menuBar)
    def createMenu(self,menuItem):
        menu = wx.Menu()
        for menuName,menuStatus,menuHandler in menuItem:
            if not menuName:
                menu.AppendSeparator()
                continue
            theMenu=menu.Append(wx.NewId(),menuName,menuStatus)
            self.Bind(wx.EVT_MENU,menuHandler,theMenu)
        return menu

    def buttonData(self):
        return (("First",self.OnFirst),
                ("<<PREV",self.OnPrev),
                ("NEXT>>",self.OnNext),
                ("Last",self.OnLast))
    def createButtonBar(self,panel,yPos=0):
        xPos = 0
        for name,handler in self.buttonData():
            pos = (xPos,yPos)
            button = self.buildOneButton(panel,name,handler,pos)
            xPos += button.GetSize().width           
    def buildOneButton(self,parent,label,handler,pos=(0,0)):
        button = wx.Button(parent,wx.NewId(),label,pos)
        self.Bind(wx.EVT_BUTTON,handler,button)
        return button

    def textFieldData(self):
        return (("First Name",(10,50)),
                ("Last Name",(10,80)))
    def createTextFields(self,panel):
        for eachLabel,eachPos in self.textFieldData():
            self.createCaptionedText(panel,eachLabel,eachPos)                
    def createCaptionedText(self,panel,label,pos=(0,0)):
        static = wx.StaticText(panel,wx.NewId(),label,pos)
        static.SetBackgroundColour('Black')
        textPos = (pos[0]+75,pos[1])
        wx.TextCtrl(panel,wx.NewId(),"",size=(100,-1),pos=textPos)

    def OnOpen(self,event):print('Open')
    def OnQuit(self,event):print('Quit')
    def OnCopy(self,event):print('Copy')
    def OnCut(self,event):print('Cut')
    def OnPaste(self,event):print('Paste')
    def OnOptions(self,event):print('Options...')
    def OnFirst(self,event):print('Button [First]')
    def OnPrev(self,event):print('Button [<<PREV]')
    def OnNext(self,event):print('Button [NEXT>>]')
    def OnLast(self,event):print('Button [Last]')
class App(wx.App):
    def OnInit(self):
        self.frame = RefactorFrame(None,-1)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
