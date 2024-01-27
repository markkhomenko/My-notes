#Boa:Dialog:MenuClienteMascota
"""
Created on Mon Sep 28 21:06:21 2015

@author: Win7Ultimate
"""

import wx

def create(parent):
    return MenuClienteMascota(parent)

[wxID_MENUCLIENTEMASCOTA, wxID_MENUCLIENTEMASCOTABUTTON1, 
 wxID_MENUCLIENTEMASCOTABUTTONAATRAS, wxID_MENUCLIENTEMASCOTABUTTONAGUARDAR, 
 wxID_MENUCLIENTEMASCOTABUTTONBUSCAR, wxID_MENUCLIENTEMASCOTABUTTONMATRAS, 
 wxID_MENUCLIENTEMASCOTABUTTONMODIFICARCLIENTE, 
 wxID_MENUCLIENTEMASCOTABUTTONMODIFICARMASCOTA, 
 wxID_MENUCLIENTEMASCOTACOMBOBOXRAZA, wxID_MENUCLIENTEMASCOTANOTEBOOK1, 
 wxID_MENUCLIENTEMASCOTAPANEL1, wxID_MENUCLIENTEMASCOTAPANEL2, 
 wxID_MENUCLIENTEMASCOTASTATICBOXACLIENTE, 
 wxID_MENUCLIENTEMASCOTASTATICBOXAMASCOTA, 
 wxID_MENUCLIENTEMASCOTASTATICBOXMCLIENTE, 
 wxID_MENUCLIENTEMASCOTASTATICBOXMMASCOTA, wxID_MENUCLIENTEMASCOTASTATICTEXT1, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTAAPE, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTACODIGO, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTADIREC, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTADOC, wxID_MENUCLIENTEMASCOTASTATICTEXTANOM, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTANOMMASCOTA, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTAPE, wxID_MENUCLIENTEMASCOTASTATICTEXTAPESO, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTARAZA, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTATEL, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTDIREC, wxID_MENUCLIENTEMASCOTASTATICTEXTDOC, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTMNOMMASCOTA, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTMPESO, wxID_MENUCLIENTEMASCOTASTATICTEXTNOM, 
 wxID_MENUCLIENTEMASCOTASTATICTEXTTEL, wxID_MENUCLIENTEMASCOTATEXTAAPE, 
 wxID_MENUCLIENTEMASCOTATEXTACODIGO, wxID_MENUCLIENTEMASCOTATEXTADIREC, 
 wxID_MENUCLIENTEMASCOTATEXTADOC, wxID_MENUCLIENTEMASCOTATEXTANOM, 
 wxID_MENUCLIENTEMASCOTATEXTANOMMASCOTA, wxID_MENUCLIENTEMASCOTATEXTAPESO, 
 wxID_MENUCLIENTEMASCOTATEXTATEL, wxID_MENUCLIENTEMASCOTATEXTCTRL1, 
 wxID_MENUCLIENTEMASCOTATEXTMAPE, wxID_MENUCLIENTEMASCOTATEXTMDIREC, 
 wxID_MENUCLIENTEMASCOTATEXTMDOC, wxID_MENUCLIENTEMASCOTATEXTMNOM, 
 wxID_MENUCLIENTEMASCOTATEXTMNOMMASCOTA, wxID_MENUCLIENTEMASCOTATEXTMPESO, 
 wxID_MENUCLIENTEMASCOTATEXTMTEL, 
] = [wx.NewId() for _init_ctrls in range(49)]

class MenuClienteMascota(wx.Dialog):
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False, text='Altas')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text='Modificar')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_MENUCLIENTEMASCOTA,
              name=u'MenuClienteMascota', parent=prnt, pos=wx.Point(419, 205),
              size=wx.Size(713, 485), style=wx.DEFAULT_DIALOG_STYLE,
              title=u'Cliente')
        self.SetClientSize(wx.Size(697, 447))

        self.notebook1 = wx.Notebook(id=wxID_MENUCLIENTEMASCOTANOTEBOOK1,
              name='notebook1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(697, 440), style=0)
        self.notebook1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))

        self.panel1 = wx.Panel(id=wxID_MENUCLIENTEMASCOTAPANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 414),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wx.Panel(id=wxID_MENUCLIENTEMASCOTAPANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(689, 414),
              style=wx.TAB_TRAVERSAL)

        self.staticBoxACliente = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOXACLIENTE,
              label=u'Alta Cliente', name=u'staticBoxACliente',
              parent=self.panel1, pos=wx.Point(6, 8), size=wx.Size(306, 328),
              style=0)
        self.staticBoxACliente.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Arial'))

        self.staticTextAdoc = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTADOC,
              label=u'Documento', name=u'staticTextAdoc', parent=self.panel1,
              pos=wx.Point(30, 50), size=wx.Size(55, 13), style=0)

        self.staticTextANom = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTANOM,
              label=u'Nombre', name=u'staticTextANom', parent=self.panel1,
              pos=wx.Point(30, 100), size=wx.Size(38, 13), style=0)

        self.staticTextAApe = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTAAPE,
              label=u'Apellido', name=u'staticTextAApe', parent=self.panel1,
              pos=wx.Point(30, 150), size=wx.Size(38, 13), style=0)

        self.staticTextADirec = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTADIREC,
              label=u'Direccion', name=u'staticTextADirec', parent=self.panel1,
              pos=wx.Point(30, 200), size=wx.Size(44, 13), style=0)

        self.staticTextATel = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTATEL,
              label=u'Telefono', name=u'staticTextATel', parent=self.panel1,
              pos=wx.Point(30, 250), size=wx.Size(43, 13), style=0)

        self.textANom = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTANOM,
              name=u'textANom', parent=self.panel1, pos=wx.Point(88, 100),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textADoc = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTADOC,
              name=u'textADoc', parent=self.panel1, pos=wx.Point(88, 50),
              size=wx.Size(104, 21), style=0, value=u'')

        self.textAApe = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTAAPE,
              name=u'textAApe', parent=self.panel1, pos=wx.Point(88, 150),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textADirec = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTADIREC,
              name=u'textADirec', parent=self.panel1, pos=wx.Point(88, 200),
              size=wx.Size(136, 21), style=0, value=u'')

        self.textATel = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTATEL,
              name=u'textATel', parent=self.panel1, pos=wx.Point(88, 250),
              size=wx.Size(136, 21), style=0, value=u'')

        self.staticBoxAMascota = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOXAMASCOTA,
              label=u'Alta Mascota', name=u'staticBoxAMascota',
              parent=self.panel1, pos=wx.Point(352, 8), size=wx.Size(328, 328),
              style=0)
        self.staticBoxAMascota.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Arial'))

        self.staticTextANomMascota = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTANOMMASCOTA,
              label=u'Nombre', name=u'staticTextANomMascota',
              parent=self.panel1, pos=wx.Point(368, 50), size=wx.Size(38, 13),
              style=0)

        self.staticTextARaza = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTARAZA,
              label=u'Raza', name=u'staticTextARaza', parent=self.panel1,
              pos=wx.Point(368, 100), size=wx.Size(25, 13), style=0)

        self.staticTextAPeso = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTAPESO,
              label=u'Peso', name=u'staticTextAPeso', parent=self.panel1,
              pos=wx.Point(368, 150), size=wx.Size(24, 13), style=0)

        self.staticTextACodigo = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTACODIGO,
              label=u'Codigo', name=u'staticTextACodigo', parent=self.panel1,
              pos=wx.Point(368, 200), size=wx.Size(34, 13), style=0)

        self.textANomMascota = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTANOMMASCOTA,
              name=u'textANomMascota', parent=self.panel1, pos=wx.Point(432,
              50), size=wx.Size(160, 21), style=0, value=u'')

        self.textAPeso = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTAPESO,
              name=u'textAPeso', parent=self.panel1, pos=wx.Point(432, 150),
              size=wx.Size(56, 21), style=0, value=u'')

        self.textACodigo = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTACODIGO,
              name=u'textACodigo', parent=self.panel1, pos=wx.Point(432, 200),
              size=wx.Size(128, 21), style=0, value=u'')
        self.textACodigo.SetEditable(False)

        self.buttonAGuardar = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONAGUARDAR,
              label=u'Guardar', name=u'buttonAGuardar', parent=self.panel1,
              pos=wx.Point(560, 344), size=wx.Size(115, 48), style=0)

        self.buttonAAtras = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONAATRAS,
              label=u'Atras', name=u'buttonAAtras', parent=self.panel1,
              pos=wx.Point(16, 376), size=wx.Size(88, 31), style=0)
        self.buttonAAtras.Bind(wx.EVT_BUTTON, self.OnButtonAAtrasButton,
              id=wxID_MENUCLIENTEMASCOTABUTTONAATRAS)

        self.comboBoxRaza = wx.ComboBox(choices=["Pointer", "Bulldog",
              "Bull Terrie", "Boxer", "Collie", "Dalmata", "Dogo", "Doberman",
              "Fox Terrier", "Golden", "Pastor Aleman", "Rottweiler", "Setter",
              "Pit bull","Pichichen" ], id=wxID_MENUCLIENTEMASCOTACOMBOBOXRAZA,
              name=u'comboBoxRaza', parent=self.panel1, pos=wx.Point(432, 104),
              size=wx.Size(160, 21), style=0, value=u'Seleccione la raza..')
        self.comboBoxRaza.SetLabel(u'Seleccione la raza..')
        self.comboBoxRaza.Bind(wx.EVT_COMBOBOX, self.OnComboBox1Combobox,
              id=wxID_MENUCLIENTEMASCOTACOMBOBOXRAZA)

        self.staticBoxMMascota = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOXMMASCOTA,
              label=u'Modificar Mascota', name=u'staticBoxMMascota',
              parent=self.panel2, pos=wx.Point(344, 16), size=wx.Size(328, 320),
              style=0)
        self.staticBoxMMascota.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticBoxMCliente = wx.StaticBox(id=wxID_MENUCLIENTEMASCOTASTATICBOXMCLIENTE,
              label=u'Modificar Cliente', name=u'staticBoxMCliente',
              parent=self.panel2, pos=wx.Point(8, 8), size=wx.Size(312, 328),
              style=0)
        self.staticBoxMCliente.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticTextDoc = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTDOC,
              label=u'Documento', name=u'staticTextDoc', parent=self.panel2,
              pos=wx.Point(32, 56), size=wx.Size(55, 13), style=0)

        self.textMDoc = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMDOC,
              name=u'textMDoc', parent=self.panel2, pos=wx.Point(96, 56),
              size=wx.Size(112, 21), style=0, value=u'')

        self.buttonBuscar = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONBUSCAR,
              label=u'Buscar', name=u'buttonBuscar', parent=self.panel2,
              pos=wx.Point(220, 55), size=wx.Size(75, 23), style=0)

        self.textMNom = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMNOM,
              name=u'textMNom', parent=self.panel2, pos=wx.Point(95, 120),
              size=wx.Size(100, 21), style=0, value=u'')

        self.textMApe = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMAPE,
              name=u'textMApe', parent=self.panel2, pos=wx.Point(95, 170),
              size=wx.Size(100, 21), style=0, value=u'')

        self.textMTel = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMTEL,
              name=u'textMTel', parent=self.panel2, pos=wx.Point(95, 220),
              size=wx.Size(100, 21), style=0, value=u'')

        self.textMDirec = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMDIREC,
              name=u'textMDirec', parent=self.panel2, pos=wx.Point(95, 270),
              size=wx.Size(100, 21), style=0, value=u'')

        self.staticTextNom = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTNOM,
              label=u'Nombre', name=u'staticTextNom', parent=self.panel2,
              pos=wx.Point(25, 120), size=wx.Size(38, 13), style=0)

        self.staticTextApe = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTAPE,
              label=u'Apellido', name=u'staticTextApe', parent=self.panel2,
              pos=wx.Point(25, 170), size=wx.Size(38, 13), style=0)

        self.staticTextTel = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTTEL,
              label=u'Telefono', name=u'staticTextTel', parent=self.panel2,
              pos=wx.Point(25, 220), size=wx.Size(43, 13), style=0)

        self.staticTextDirec = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTDIREC,
              label=u'Direccion', name=u'staticTextDirec', parent=self.panel2,
              pos=wx.Point(25, 270), size=wx.Size(44, 13), style=0)

        self.buttonModificarCliente = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONMODIFICARCLIENTE,
              label=u'Modificar', name=u'buttonModificarCliente',
              parent=self.panel2, pos=wx.Point(232, 304), size=wx.Size(75, 23),
              style=0)
        

        self.buttonModificarMascota = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONMODIFICARMASCOTA,
              label=u'Modificar', name=u'buttonModificarMascota',
              parent=self.panel2, pos=wx.Point(568, 304), size=wx.Size(75, 23),
              style=0)

        self.buttonMAtras = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTONMATRAS,
              label=u'Atras', name=u'buttonMAtras', parent=self.panel2,
              pos=wx.Point(16, 376), size=wx.Size(88, 31), style=0)
        self.buttonMAtras.Bind(wx.EVT_BUTTON, self.OnButtonMAtrasButton,
              id=wxID_MENUCLIENTEMASCOTABUTTONMATRAS)

        self.button1 = wx.Button(id=wxID_MENUCLIENTEMASCOTABUTTON1,
              label=u'Buscar', name='button1', parent=self.panel2,
              pos=wx.Point(520, 55), size=wx.Size(75, 23), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTCTRL1,
              name='textCtrl1', parent=self.panel2, pos=wx.Point(408, 56),
              size=wx.Size(100, 21), style=0, value=u'')

        self.staticText1 = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXT1,
              label=u'Codigo', name='staticText1', parent=self.panel2,
              pos=wx.Point(360, 56), size=wx.Size(34, 13), style=0)

        self.textMNomMascota = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMNOMMASCOTA,
              name=u'textMNomMascota', parent=self.panel2, pos=wx.Point(424,
              128), size=wx.Size(100, 21), style=0, value=u'')

        self.textMPeso = wx.TextCtrl(id=wxID_MENUCLIENTEMASCOTATEXTMPESO,
              name=u'textMPeso', parent=self.panel2, pos=wx.Point(424, 185),
              size=wx.Size(100, 21), style=0, value=u'')

        self.staticTextMNomMascota = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTMNOMMASCOTA,
              label=u'Nombre', name=u'staticTextMNomMascota',
              parent=self.panel2, pos=wx.Point(360, 128), size=wx.Size(38, 13),
              style=0)

        self.staticTextMPeso = wx.StaticText(id=wxID_MENUCLIENTEMASCOTASTATICTEXTMPESO,
              label=u'Peso', name=u'staticTextMPeso', parent=self.panel2,
              pos=wx.Point(360, 185), size=wx.Size(24, 13), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)
        
    def OnButtonAAtrasButton(self, event):
        self.Close(True)

    def OnComboBox1Combobox(self, event):
        event.Skip()    
        
    def OnButtonMAtrasButton(self, event):
        self.Close(True)
        
    
    def __init__(self, parent):
        self._init_ctrls(parent)