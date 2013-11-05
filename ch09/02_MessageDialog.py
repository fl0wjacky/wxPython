#! /usr/bin/env python
# coding:utf-8

import wx
import wx.lib.dialogs as wd

if __name__ == "__main__":
    app = wx.PySimpleApp()

    # 方法一 使用类
    dlg = wx.MessageDialog(None,"Is this explanation OK?",
        'A Message Box',wx.YES_NO | wx.ICON_QUESTION)
    retCode = dlg.ShowModal()
    if (retCode == wx.ID_YES):
        print "Yes"
    else:
        print "No"
    dlg.Destroy()

    # 方法二 使用函数
    retCode = wx.MessageBox('Is the way easier?','Via Function',wx.YES_NO | wx.ICON_QUESTION)
    
    # 方法三 使用Python特定的类（只显示一个OK按钮）
    message = '1999年春天，当《圣何塞信使新闻报》的星期日增刊让我去采访Linux Torvals时，我对他只有一些模糊的了解。在这年的春天的早些时候，随着一系列的公司和网景公司一样采用了公开源代码概念或者干脆采用了Linux操作系统本身，Linus一时间成了一个众人皆知的名字。尽管我对于这方面的发展并不十分了解，但在九十年代初期，我在一本涉及到UNIX操作系统和公开源代码问题的杂志担任编辑，所以我脑子里还残留着一些相当的记忆：包括Linus是个芬兰的大学生，他在自己的宿舍里编写了一个影响极大的UNIX系统，并且免费在互联网上散发，等等。这些信息并非十分准确。给我打电话的编辑说，在最近于圣和塞举办的Linux展览上，Linus已经成为众星捧月的核心人物，所以他督促我一定要完成这项任务：”我现在手头有一个闻名全球的超级明星，就在这里，奧，不，在圣克拉拉。“接着他便把一些报纸简报传真给了我。\nLinus已经在两年前来到了硅谷，正在为当时还显得特别神秘的Transmeta公司工作，那家公司多年来一直致力于开发一种据说成功后将轰动整个电脑工业的微处理器。但是，不知何故，Transmeta公司却允许Linus继续他那项耗时甚多的工作，他仍旧是Linux的最高领袖，对着个操作系统的任何修改拥有最终的决定权（事实上，他的追随者已经在着手进行法律方面的工作，以期在法律上让他成为Linux商标的所有者）。此外，他还有时间在全球四处旅游，为方兴未艾的公开源代码运动大作宣传。'
    wd.ScrolledMessageDialog(None,message,'Linus Torvals').ShowModal()
