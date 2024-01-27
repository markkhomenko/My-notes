#Boa:Dialog:MenuPaseador

import wx

def create(parent):
    return MenuPaseador(parent)

[wxID_MENUPASEADOR, wxID_MENUPASEADORBOTONATRAS, wxID_MENUPASEADORBOTONATRAS2, 
 wxID_MENUPASEADORBOTONBUSCARP, wxID_MENUPASEADORBOTONGUARDARP, 
 wxID_MENUPASEADORBOTONMODIFICAR, wxID_MENUPASEADORBOXALTAP, 
 wxID_MENUPASEADORNOTEBOOK1, wxID_MENUPASEADORPANEL1, wxID_MENUPASEADORPANEL2, 
 wxID_MENUPASEADORSTATICBOX1, wxID_MENUPASEADORSTATICTEXTAPEP, 
 wxID_MENUPASEADORSTATICTEXTDOCP, wxID_MENUPASEADORSTATICTEXTMODAPEP, 
 wxID_MENUPASEADORSTATICTEXTMODNOMP, wxID_MENUPASEADORSTATICTEXTMODTELP, 
 wxID_MENUPASEADORSTATICTEXTNOMP, wxID_MENUPASEADORSTATICTEXTTELP, 
 wxID_MENUPASEADORTEXTCTRLAPEP, wxID_MENUPASEADORTEXTCTRLMODAPEP, 
 wxID_MENUPASEADORTEXTCTRLMODNOMP, wxID_MENUPASEADORTEXTCTRLMODTELP, 
 wxID_MENUPASEADORTEXTCTRLNOMP, wxID_MENUPASEADORTEXTCTRLTELP, 
 wxID_MENUPASEADORTEXTDOCP, 
] = [wx.NewId() for _init_ctrls in range(25)]

class MenuPaseador(wx.Dialog):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'Altas')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text=u'Modificar')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MENUPASEADOR, name=u'MenuPaseador',
              parent=prnt, pos=wx.Point(396, 166), size=wx.Size(713, 485),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Paseador')
        self.SetClientSize(wx.Size(705, 454))

        self.notebook1 = wx.Notebook(id=wxID_MENUPASEADORNOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(704, 456), style=0)

        self.panel1 = wx.Panel(id=wxID_MENUPASEADORPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(696, 430),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_MENUPASEADORPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(696, 430),
              style=wx.TAB_TRAVERSAL)

        self.BoxAltaP = wx.StaticBox(id=wxID_MENUPASEADORBOXALTAP,
              label=u'Alta Paseador', name=u'BoxAltaP', parent=self.panel1,
              pos=wx.Point(24, 24), size=wx.Size(432, 328), style=0)
        self.BoxAltaP.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticTextDocP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTDOCP,
              label=u'Documento', name=u'staticTextDocP', parent=self.panel1,
              pos=wx.Point(48, 64), size=wx.Size(55, 13), style=0)
        self.staticTextDocP.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.textDocP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTDOCP,
              name=u'textDocP', parent=self.panel1, pos=wx.Point(144, 64),
              size=wx.Size(136, 21), style=0, value=u'')

        self.botonBuscarP = wx.Button(id=wxID_MENUPASEADORBOTONBUSCARP,
              label=u'Buscar', name=u'botonBuscarP', parent=self.panel1,
              pos=wx.Point(328, 64), size=wx.Size(75, 23), style=0)
        self.botonBuscarP.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.botonBuscarP.Bind(wx.EVT_BUTTON, self.OnBotonBuscarPButton,
              id=wxID_MENUPASEADORBOTONBUSCARP)

        self.staticTextNomP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTNOMP,
              label=u'Nombre', name=u'staticTextNomP', parent=self.panel1,
              pos=wx.Point(48, 152), size=wx.Size(38, 13), style=0)
        self.staticTextNomP.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.staticTextApeP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTAPEP,
              label=u'Apellido', name=u'staticTextApeP', parent=self.panel1,
              pos=wx.Point(48, 208), size=wx.Size(38, 13), style=0)

        self.staticTextTelP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTTELP,
              label=u'Telefono', name=u'staticTextTelP', parent=self.panel1,
              pos=wx.Point(48, 264), size=wx.Size(43, 13), style=0)

        self.textCtrlNomP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLNOMP,
              name=u'textCtrlNomP', parent=self.panel1, pos=wx.Point(144, 152),
              size=wx.Size(112, 21), style=0, value=u'')

        self.textCtrlApeP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLAPEP,
              name=u'textCtrlApeP', parent=self.panel1, pos=wx.Point(144, 208),
              size=wx.Size(112, 21), style=0, value=u'')

        self.textCtrlTelP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLTELP,
              name=u'textCtrlTelP', parent=self.panel1, pos=wx.Point(144, 264),
              size=wx.Size(112, 21), style=0, value=u'')

        self.botonGuardarP = wx.Button(id=wxID_MENUPASEADORBOTONGUARDARP,
              label=u'Guardar', name=u'botonGuardarP', parent=self.panel1,
              pos=wx.Point(576, 368), size=wx.Size(99, 47), style=0)
        self.botonGuardarP.Bind(wx.EVT_BUTTON, self.OnBotonGuardarButton,
              id=wxID_MENUPASEADORBOTONGUARDARP)

        self.BotonAtras = wx.Button(id=wxID_MENUPASEADORBOTONATRAS,
              label=u'Atras', name=u'BotonAtras', parent=self.panel1,
              pos=wx.Point(24, 392), size=wx.Size(75, 23), style=0)
        self.BotonAtras.Bind(wx.EVT_BUTTON, self.OnBotonAtrasButton,
              id=wxID_MENUPASEADORBOTONATRAS)

        self.staticBox1 = wx.StaticBox(id=wxID_MENUPASEADORSTATICBOX1,
              label=u'Modificar Paseador', name='staticBox1',
              parent=self.panel2, pos=wx.Point(24, 24), size=wx.Size(432, 328),
              style=0)
        self.staticBox1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticTextModNomP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTMODNOMP,
              label=u'Nombre', name=u'staticTextModNomP', parent=self.panel2,
              pos=wx.Point(56, 88), size=wx.Size(38, 13), style=0)

        self.staticTextModApeP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTMODAPEP,
              label=u'Apellido', name=u'staticTextModApeP', parent=self.panel2,
              pos=wx.Point(56, 160), size=wx.Size(38, 13), style=0)

        self.staticTextModTelP = wx.StaticText(id=wxID_MENUPASEADORSTATICTEXTMODTELP,
              label=u'Telefono', name=u'staticTextModTelP', parent=self.panel2,
              pos=wx.Point(56, 232), size=wx.Size(43, 13), style=0)

        self.BotonAtras2 = wx.Button(id=wxID_MENUPASEADORBOTONATRAS2,
              label=u'Atras', name=u'BotonAtras2', parent=self.panel2,
              pos=wx.Point(24, 392), size=wx.Size(75, 23), style=0)
        self.BotonAtras2.Bind(wx.EVT_BUTTON, self.OnBotonAtras2Button,
              id=wxID_MENUPASEADORBOTONATRAS2)

        self.botonModificar = wx.Button(id=wxID_MENUPASEADORBOTONMODIFICAR,
              label=u'Modificar', name=u'botonModificar', parent=self.panel2,
              pos=wx.Point(368, 312), size=wx.Size(75, 23), style=0)
        self.botonModificar.Bind(wx.EVT_BUTTON, self.OnBotonModificarButton,
              id=wxID_MENUPASEADORBOTONMODIFICAR)

        self.textCtrlModNomP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLMODNOMP,
              name=u'textCtrlModNomP', parent=self.panel2, pos=wx.Point(168,
              88), size=wx.Size(100, 21), style=0, value=u'')

        self.textCtrlModApeP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLMODAPEP,
              name=u'textCtrlModApeP', parent=self.panel2, pos=wx.Point(168,
              160), size=wx.Size(100, 21), style=0, value=u'')

        self.textCtrlModTelP = wx.TextCtrl(id=wxID_MENUPASEADORTEXTCTRLMODTELP,
              name=u'textCtrlModTelP', parent=self.panel2, pos=wx.Point(168,
              232), size=wx.Size(100, 21), style=0, value=u'')

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonBuscarPButton(self, event):
        event.Skip()

    def OnBotonGuardarButton(self, event):
        event.Skip()
        
    def OnBotonAtrasButton(self, event):
        self.Close(True)

    def OnBotonAtras2Button(self, event):
        self.Close(True)

    def OnBotonModificarButton(self, event):
        event.Skip()

    
