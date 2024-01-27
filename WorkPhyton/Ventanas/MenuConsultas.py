# -*- coding: utf-8 -*-

import wx
import wx.grid


def create(parent):
    return MenuConsultas(parent)

[wxID_MENUCONSULTAS, wxID_MENUCONSULTASGRID1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class MenuConsultas(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MENUCONSULTAS, name=u'MenuConsultas',
              parent=prnt, pos=wx.Point(463, 158), size=wx.Size(400, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Consultas')
        self.SetClientSize(wx.Size(384, 447))

        self.grid1 = wx.grid.Grid(id=wxID_MENUCONSULTASGRID1, name='grid1',
              parent=self, pos=wx.Point(88, 80), size=wx.Size(200, 100),
              style=0)
        self.grid1.SetCellValue(0,1, self.grid1.lista_cliente[0][5])

    def __init__(self, parent):
        self._init_ctrls(parent)
