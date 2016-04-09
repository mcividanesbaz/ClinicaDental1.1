__author__ = 'Marcos Cividanes'

from gi.repository import Gtk
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle

import sqlite3 as dbapi


class Clinica(Gtk.Window):
   # Este es el constructor principal
    def __init__(self):

        #creamos la interfaz con Gtk
        #Creamos la conexion a la base de datos
        #Creamos el Listbox, y iniciamos la lista de rows
        #Creamos la cantidad de rows necesarias, labels, botones y entrys

        self.condicion = bool
        self.bd = dbapi.connect("clinica.dat")
        self.cursor = self.bd.cursor()
        self.elementos = []
        self.pacientes=""
        #self.cursor.execute("CREATE TABLE CLINICA (DNI VARCHAR(7) PRIMARY KEY NOT NULL,"
         #                   "NOMBRE VARCHAR(20),"
          #                  "TELEFONO VARCHAR(9),"
           #                 "SEGURO VARCHAR(50),"
            #                "TRATAMIENTO VARCHAR(30))")
        Gtk.Window.__init__(self, title="Clinica Dental")
        self.set_border_width(20)
        self.set_default_size(500, 100)

        self.caja = Gtk.Box(spacing=6)
        self.caja.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(self.caja)

        self.listacaja = Gtk.ListBox()
        self.listacaja.set_selection_mode(Gtk.SelectionMode.NONE)
        print(self.listacaja.get_selection_mode())
        self.caja.pack_start(self.listacaja, True, True, 0)

        # PRIMERA FILA
        self.fila1 = Gtk.ListBoxRow()
        self.cajah = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila1.add(self.cajah)
        self.cajav = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.cajah.pack_start(self.cajav, True, True, 1)

        # SEGUNDA FILA
        self.fila2 = Gtk.ListBoxRow()
        self.cajah2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila2.add(self.cajah2)
        self.cajav2 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.cajah2.pack_start(self.cajav2, True, True, 1)

        # TERCERA FILA
        self.fila3 = Gtk.ListBoxRow()
        self.hor_box3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila3.add(self.hor_box3)
        self.cajav3 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box3.pack_start(self.cajav3, True, True, 1)

        # CUARTA FILA
        self.fila4 = Gtk.ListBoxRow()
        self.hor_box4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila4.add(self.hor_box4)
        self.cajav4 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.hor_box4.pack_start(self.cajav4, True, True, 1)

        # QUINTA FILA

        self.fila5 = Gtk.ListBoxRow()
        self.cajah5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila5.add(self.cajah5)
        self.cajav5 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.cajah5.pack_start(self.cajav5, True, True, 1)

        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.vista = Gtk.TreeView()
        self.cajav5.add(self.scroll)
        self.scroll.add(self.vista)
        self.scroll.set_size_request(500, 500)
        self.scroll.show()

        self.lista = Gtk.ListStore(str, str, str, str, str)

        for i in self.cursor:
            self.lista.append(i)

        self.vista.set_model(self.lista)

        for i, title in enumerate(["DNI","NOMBRE","TELEFONO","SEGURO","TRATAMIENTO"]):
            render = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(title, render, text=i)
            self.vista.append_column(columna)


        # Row6
        self.fila6 = Gtk.ListBoxRow()
        self.cajah6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila6.add(self.cajah6)
        self.cajav5 = Gtk.Box(Gtk.Orientation.VERTICAL)
        self.cajah6.pack_start(self.cajav5, True, True, 1)

        self.preciot=0
        self.cantidadcompra=0

        self.labeldni = Gtk.Label("DNI: ")
        self.labelnom = Gtk.Label("NOMBRE: ")
        self.labeltel = Gtk.Label("TELEFONO:")
        self.labelseg = Gtk.Label("SEGURO: ")
        self.labeltrat = Gtk.Label("TRATAMIENTO:")
        self.labelist = Gtk.Label(" ")
        self.labelespacio=Gtk.Label(" ")

        self.dni = Gtk.Entry()
        self.nom = Gtk.Entry()
        self.tel = Gtk.Entry()
        self.seg = Gtk.Entry()
        self.trat= Gtk.Entry()


        self.verpb = Gtk.Button(label="Ver Pacientes")
        self.buscarpb = Gtk.Button(label="Buscar")
        self.nuevopb = Gtk.Button(label="Nuevo Paciente")
        self.borrarpb = Gtk.Button(label="Eliminar")
        self.modificarpb = Gtk.Button(label="Modificar")
        self.bimprimir = Gtk.Button(label="Imprimir")
        self.infob=Gtk.Button(label="Informacion")


        self.cajav.pack_start(self.labeldni, True, True, 1)
        self.cajav.pack_start(self.dni, True, True, 1)
        self.cajav.pack_start(self.labelseg, True, True, 1)
        self.cajav.pack_start(self.seg, True, True, 1)
        self.cajav2.pack_start(self.labelnom, True, True, 1)
        self.cajav2.pack_start(self.nom, True, True, 1)
        self.cajav2.pack_start(self.labeltrat, True, True, 1)
        self.cajav2.pack_start(self.trat, True, True, 1)
        self.cajav3.pack_start(self.labeltel, True, True, 1)
        self.cajav3.pack_start(self.tel, True, True, 1)
        self.cajav3.pack_start(self.verpb, True, True, 1)
        self.cajav3.pack_start(self.modificarpb, True, True, 1)
        self.cajav4.pack_start(self.bimprimir, True, True, 1)
        self.cajav4.pack_start(self.infob, True, True, 1)
        self.cajav4.pack_start(self.nuevopb, True, True, 1)
        self.cajav4.pack_start(self.borrarpb, True, True, 1)


        self.listacaja.add(self.fila1)
        self.listacaja.add(self.fila2)
        self.listacaja.add(self.fila3)
        self.listacaja.add(self.fila4)
        self.listacaja.add(self.fila5)
        self.listacaja.add(self.fila6)


        self.verpb.connect("clicked", self.verpacientes)
        self.nuevopb.connect("clicked", self.nuevop)
        self.borrarpb.connect("clicked", self.borrarp)
        self.modificarpb.connect("clicked", self.modificarp)
        self.bimprimir.connect("clicked",self.imprimir)
        self.buscarpb.connect("clicked", self.buscarp)
        self.infob.connect("clicked", self.info)


#Metodo Ver

    def verpacientes(self,widget):

       # Sirve para mostrar el contenido de la base de datos

        self.lista.clear()
        self.cursor.execute("select * from clinica")
        for e in self.cursor:
            self.lista.append(e)
            print(e)
        self.vista.set_model(self.lista)


#Metodo Buscar

    def buscarp(self,widget):

        # Busca un paciente en la base mediante el dni

        dni= self.dni.get_text()
        if dni.isdigit:
            self.condicion=True
            self.cursor.execute("select * from clinica where dni='"+dni+"'")
            for res in self.cursor:
                 self.pacientes=self.pacientes+("DNI: " + str(res[0]) + ", "
                                     "NOMBRE: " + str(res[1]) + ", "
                                     "TELEFONO: " + str(res[2]) + ", "
                                     "SEGURO: " + str(res[3]) + ", "
                                     "TRATAMIENTO: " + str(res[4])+"\n")
            self.ventanita.set_text(self.pacientes)
            self.bd.commit()
        else:
            self.vemergente("Revise los datos")
            self.condicion=False


#Metodo de Informacion sobre el programa
    def info(self,widget):
        self.ventanita("Informacion al usuario")


#Metodo Modificar

    def modificarp(self,widget):

        #Modifica camp en la base de datos mediante el dni

        dni = str(self.dni.get_text())
        nom = str(self.nom.get_text())
        tel = str(self.tel.get_text())
        seg = str(self.seg.get_text())
        trat = str(self.seg.get_text())

        if dni.isdigit and nom.isalpha and tel.isdigit:
            self.condicion = True
        else:
            self.ventanita("DNI,NOMBRE O TELEFONO INVALIDO")
            self.condicion = False

        if (self.condicion):

            self.cursor.execute("update clinica set nombre ='" + nom + "'"
                                                     ",telefono='" + tel + "'"
                                                     ",seguro='" + seg + "'"
                                                     ",tratamiento='" + trat + "'"
                                                     " where dni='" + dni + "'")
            self.bd.commit()
            self.ventanita("MODIFICADO")


#Metodo Borrar

    def borrarp(self,widget):


       #Borra un paciente de la base de datos

        dni=self.dni.get_text()
        selection = self.vista.get_selection()
        model, selecion = selection.get_selected()
        if selecion != None:
            self.dni = model[selecion][0]
        if dni.isdigit:
            self.cursor.execute("DELETE FROM CLINICA WHERE='"+dni+"' ")
            self.bd.commit()
            self.verpacientes()
            self.ventanita("BORRADO")
        else:
            self.ventanita("DNI INVALIDO")
            pass

#Metodo Añadir

    def nuevop(self,widget):

        #Incluye  un nuevo paciente en la base de datos

        dni = str(self.dni.get_text())
        nom = str(self.nom.get_text())
        tel = str(self.tel.get_text())
        seg = str(self.seg.get_text())
        trat = str(self.seg.get_text())

        if dni.isdigit and nom.isalpha and tel.isdigit:
            self.condicion = True
        else:
            self.ventanita("DNI,NOMBRE O TELEFONO INVALIDO")
            self.condicion = False

        if (self.condicion):
            try:
                self.cursor.execute("INSERT INTO CLINICA VALUES('"+dni+"','"+nom+"','"+tel+"','"+seg+"','"+trat+"')")
                self.bd.commit()
                self.ventanita("INSERTADO")
            except dbapi.IntegrityError:
                self.ventanita("DNI RAPETIDO")

 #Quitar
    def quitarv(self, widget):

       #Cierra la ventana

        widget.destroy()


    def ventanita(self, texto):
       #Es una ventana emergente a la cual accedemos en los otros metodos para notificarle a los usuarios si se hicieron o no correctamente las operaciones

        window = Gtk.Window(title="ATENCION")
        label = Gtk.Label(texto)
        label.set_padding(10, 10)
        window.add(label)
        window.connect("delete-event", self.quitarv)
        window.set_position(Gtk.PositionType.RIGHT)
        window.show_all()

#Metodo Imprimir

    def imprimir(self,widget):

       #Imprime un pdf con el contenido de la base de datos en un pdf

        pdf = "Clinica Dental.pdf"
        c = canvas.Canvas(pdf, pagesize=A4)
        c.drawString(20, 800, "Clientes")
        pacientes = list(self.cursor.execute("select * from clinica"))
        title = [["DNI", "NOMBRE", "TELEFONO", "SEGURO","TRATAMIENTO"]]

        p = title + pacientes
        tabla = Table(p)

        tabla.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 2, colors.red),
                                   ('BACKGROUND', (0, 1), (-1, -1), colors.yellow),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.green)]))
        tabla.wrapOn(c, 20, 30)
        tabla.drawOn(c, 20, 600)
        c.save()
        self.ventanita("PDF LISTO")


clinicav = Clinica()
clinicav.set_position(Gtk.WindowPosition.CENTER)
clinicav.set_resizable(False)
clinicav.connect("delete-event", Gtk.main_quit)
clinicav.show_all()
Gtk.main()