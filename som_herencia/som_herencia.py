# -*- coding: utf-8 -*-
from osv import osv, fields
from tools.translate import _
from tools import config
import netsvc
try:
    from collections import OrderedDict
except:
    from ordereddict import OrderedDict

class ClasseVehicle(osv.osv):
    '''
    Classe mare vehicle per fer proves d'herència
    '''
    _name = 'classe.vehicle'

    _columns = {
        'id': fields.integer('id', readonly=True),
        'name': fields.char(
            "Marca del vehicle", size=20, required=False,
            help="Marca del vehicle",),
        'matricula': fields.char(
            "Matricula", size=10, required=False, unique=True,
            help="Matricula del vehicle",),
        'data_compra': fields.date(
            "Data compra", required=True,
            help="Quin dia es va comprar",),
        'rodes': fields.integer("Nombre de rodes", required=False,)
    }

    def endavant(self):
        return "El vehicle va endavant"

    def endarrere(self):
        return "El vehicle va endarrere"

    def giraesquerra(self):
        return "El vehicle gira a l'esquerra"

    def ferhotot(self):
        return str(self.endavant() + "->" +
        self.endarrere() + "->" +
        self.giraesquerra())

ClasseVehicle()

class ClasseCotxe(osv.osv):
    '''
    Class Inheritance
    Classe filla herència classica. Afegim comportament.
    '''
    _name = 'classe.vehicle'
    _inherit = 'classe.vehicle'
    _columns = {
        'portes': fields.integer(
            "Nombre de portes")
    }

    def parabrises(self):
        return "Accionem el parabrises"

    def giraVolantEsquerra(self):
        return str("Gira el volant a l'esquerra -> " + self.giraesquerra())

ClasseCotxe()

class ClasseMoto(osv.osv):
    '''
    Inheritance by prototyping
    Classe filla herència classica. Afegim comporament
    '''
    _name = 'classe.moto'
    _inherit = 'classe.vehicle'
    _columns = {
        'cavalls': fields.integer(
            "Potencia en cavalls")
    }
    
    def fercaballet(self):
        return "Fem el caballet"

    def genollesquerra(self):
        return str(self.giraesquerra() + "-> genoll esquerra a terra")

ClasseMoto()


class ClasseAutocar(osv.osv):
    '''
    Instance inheritance
    Classe filla herència per delegació. Aniueum un registre Vehicle dins Autocar.
    Podem accedir als camps però no als mètodes
    '''
    _name = 'classe.autocar'
    _inherits = OrderedDict([('classe.vehicle', 'id_vehicle')])
    _columns = {
        #'matricula':fields.many2one('classe.vehicle','matricula',required=True),
        'id_vehicle':fields.many2one('classe.vehicle','id',required=True),
        'places': fields.integer("Nombre de places"),
    }

    def giraVolantEsquerra(self):
        return str("Gira el volant de l'Autocar a l'esquerra -> " + super(ClasseAutocar, self).giraesquerra())

ClasseAutocar()


class ClasseCamio(osv.OsvInherits):
    '''
    Instance inheritance
    Classe filla herència per delegació. Aniueum un registre Vehicle dins Camió
    Podem accedir als camps i als mètodes osv.OsvInherits
    '''
    _name = 'classe.camio'
    _inherits = OrderedDict([('classe.vehicle', 'id_vehicle')])
    _columns = {
        #'matricula':fields.many2one('classe.vehicle','matricula',required=True),
        'id_vehicle':fields.many2one('classe.vehicle','id',required=True),
        'capacitat': fields.integer("Capacitt en litres")
    }

    def giraVolantEsquerra(self):
        return str("Gira el volant del Camió a l'esquerra -> " + self.giraesquerra())

ClasseCamio()
