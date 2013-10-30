#! /usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from ch05_512 import ModelExample
import wx

class TestExample(unittest.TestCase):   #1.声明一个TestCase
    def setUp(self):
        self.app = wx.PySimpleApp()     #2.为每个测试所做的测试
        self.frame = ModelExample(parent=None,id = -1)

    def tearDown(self):                 #3.测试之后的清除工作
        self.frame.Destroy()

    def testModel(self):                #4.声明一个测试(Test)
        self.frame.OnBarney(None)
        self.assertEqual("Barney",self.frame.model.first,
            msg = 'First is wrong')     #5.对于可能的失败的断定
        self.assertEqual("Rubble",self.frame.model.last)

    def testEvent(self):
        panel = self.frame.GetChildren()[0]
        for each in panel.GetChildren():
            if each.GetLabel() == "Wilmafy":
                wilma = each
                break
        event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED,wilma.GetId())
        wilma.GetEventHandler().ProcessEvent(event)
        self.assertEqual("Wilma",self.frame.model.first)
        self.assertEqual("Flintstone",self.frame.model.last)

def suite():                            #6.创建一个TEstSuite
    suite = unittest.makeSuite(TestExample,'test')
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest='suite')  #7.开始测试
