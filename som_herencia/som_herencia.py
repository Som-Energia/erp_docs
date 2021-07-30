# -*- coding: utf-8 -*-
from osv import osv, fields
from tools.translate import _
from tools import config
from datetime import datetime
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
        'rodes': fields.integer("Nombre de rodes", required=False,),
        'data_revisio': fields.date(
                       "Data revisió", required=False,
                        help = "Quin dia es va fer la ultima revisio",)
    }

    def endavant(self):
        return "El vehicle va endavant"

    def endarrere(self):
        return "El vehicle va endarrere"

    def giraesquerra(self):
        return "El vehicle gira a l'esquerra"

    def giraDreta(self):
        return "El vehicle gira a la dreta"

    def ferhotot(self):
        return str(self.endavant() + "->" +
        self.endarrere() + "->" +
        self.giraesquerra())

    def passarRevisio(self,cursor,uid,id):
        vehicle = self.browse(cursor,uid,id)
        today=datetime.today()
        vehicle.write({'data_revisio': today.strftime("%Y-%m-%d")})
        return "Revisio passada el " + str(vehicle.data_revisio)

    def parabrises(self):
        return "Accionem el parabrises"


ClasseVehicle()

class ClasseCotxe(osv.osv):
    '''
    Class Inheritance
    Classe filla herència classica. La fem servir per afegir comportament a un model existent, sense crear cap model nou. 
    Coneguts com a mòduls "Custom".
    '''
    _name = 'classe.vehicle'
    _inherit = 'classe.vehicle'
    _columns = {
        'portes': fields.integer(
            "Nombre de portes")
    }

    # Serà accessible des de tots els Vehicles
    def parabrises(self):
        return "Accionem el parabrises"

    # Serà accessible des de tots els Vehicles
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
    
    #Accedim a un camp del registre actual
    def fercaballet(self, cursor, uid, id):
        moto = self.browse(cursor, uid, id)
        return "Fem el caballet perque tenim molts cavalls -> " + str(moto.cavalls)

    #Es pot accedir als mètodes mare amb self.
    def genollesquerra(self):
        return str(self.giraesquerra() + "-> genoll esquerra a terra")

    #Es pot accedir als mètodes mare mitjançant super. Això permet reescriure comportament i cridar al mètode mare.
    def endarrere(self):
        return str(super(ClasseMoto, self).endarrere() + " -> Un moment, la moto no pot anar endarrere!")

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
        'id_vehicle':fields.many2one('classe.vehicle','id',required=True),
        'places': fields.integer("Nombre de places"),
    }

    def quantesPortesTinc(self, cr, uid, id):
        autocar = self.browse(cr, uid, id)
        return "Tinc " + str(autocar.portes) + " portes."

    #No es pot accedir als mètodes mare amb self.
    def obreMaleter(self):
        return str(self.giraDreta() + " -> Obre Maleter")

    #No es pot accedir als mètodes mare mitjançant super. Això fa que no es pot reescriure comportament i a la vegada cridar al mètode mare.
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
        'id_vehicle':fields.many2one('classe.vehicle','id',required=True),
        'capacitat': fields.integer("Capacitt en litres")
    }

    #Es pot accedir als mètodes mare amb self.
    def giraVolantEsquerra(self):
        return str("Gira el volant del Camió a l'esquerra -> " + self.giraesquerra())

    #No es pot accedir als mètodes mare mitjançant super. Això fa que no es pot reescriure comportament i a la vegada cridar al mètode mare.
    def giraDreta(self):
        return str("Camio -> " + super(ClasseCamio, self).giraDreta())

ClasseCamio()
