# -*- coding: utf-8 -*-
from destral import testing
from destral.transaction import Transaction
from destral.patch import PatchNewCursors
import netsvc
import time
import random
from datetime import datetime

class VehicleTests(testing.OOTestCase):
    def setUp(self):
        self.pool = self.openerp.pool
        self.Vehicle = self.pool.get('classe.vehicle')
        self.Moto = self.pool.get('classe.moto')
        self.Cotxe = self.pool.get('classe.vehicle')
        self.Camio = self.pool.get('classe.camio')
        self.Autocar = self.pool.get('classe.autocar')
        self.Data = self.pool.get('ir.model.data')

    def tearDown(self):
        #self.txn.stop()
        pass

    def test__passarRevisio_Vehicle(self):

        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            vehicle_id = self.Data.get_object_reference(
                        cursor, uid, 'som_herencia', 'demo_vehicle_1'
                        )[1]
            result = self.Vehicle.passarRevisio(cursor, uid, vehicle_id)
            vehicle = self.Vehicle.browse(cursor, uid, vehicle_id)

            strAvui = str(datetime.today().strftime("%Y-%m-%d"))
            self.assertEquals(
                result,
                "Revisio passada el " + strAvui
            )
            self.assertEquals(vehicle.data_revisio, strAvui )

    def test__ferHoTot_Vehicle(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Vehicle.ferhotot()

            self.assertEquals(
                result,
                "El vehicle va endavant->El vehicle va endarrere->El vehicle gira a l'esquerra"
            )

    def test__giraVolantEsquerra__Cotxe(self): 
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Cotxe.giraVolantEsquerra()

    def test__ferHoTot_Moto(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Moto.ferhotot()

            self.assertEquals(result, "El vehicle va endavant->El vehicle va endarrere -> Un moment, la moto no pot anar endarrere!->El vehicle gira a l'esquerra")

    def test__ferCaballet__Moto(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user
            #Exemple d'obtenir un element de la base de dades carregat amb el xml demo
            moto_id = self.Data.get_object_reference(
                        cursor, uid, 'som_herencia', 'demo_moto_1'
                        )[1]

            result = self.Moto.fercaballet(cursor, uid, moto_id)

            self.assertEquals(result, "Fem el caballet perque tenim molts cavalls -> 30")

    def test__genollEsquerra__Moto(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Moto.genollesquerra()

            self.assertEquals(result, "El vehicle gira a l'esquerra-> genoll esquerra a terra")

    def test__endarrere__Moto(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Moto.endarrere()

            self.assertEquals(result, "El vehicle va endarrere -> Un moment, la moto no pot anar endarrere!")

    def test__giraVolantEsquerra__Autocar(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            with self.assertRaises(AttributeError):
                # El mètode self.giraesquerra() de dins el mètode giraVolantEsquerra
                #   de la classe Vehicle no és accessible des de Autocar
                # AttributeError: 'super' object has no attribute 'giraesquerra'
                result = self.Autocar.giraVolantEsquerra()

    def test__giraVolantEsquerra__Autocar(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            with self.assertRaises(AttributeError):
                # AttributeError: 'ClasseAutocar' object has no attribute 'ferhotot'
                result = self.Autocar.ferhotot()

    def test__obreMaleter__Autocar(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            with self.assertRaises(AttributeError):
                # AttributeError: 'ClasseAutocar' object has no attribute 'giraDreta'
                result = self.Autocar.obreMaleter()

    def test__quantresPortesTinc__Autocar(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user
            #Exemple d'obtenir un element de la base de dades carregat amb el xml demo
            autocar_id = self.Data.get_object_reference(
                        cursor, uid, 'som_herencia', 'demo_autocar_1'
                        )[1]

            result = self.Autocar.quantesPortesTinc(cursor, uid, autocar_id)

            self.assertEquals(result, "Tinc 3 portes.")

    def test__giraVolantEsquerra__Camio(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Camio.giraVolantEsquerra()

            self.assertEquals(result, "Gira el volant del Camió a l'esquerra -> El vehicle gira a l'esquerra") 

    def test__ferhotot__Camio(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user
            # Gràcies al osv.OsvInherits de ClasseCamio, podem accedir als mètodes mare
            result = self.Camio.ferhotot()

            self.assertEquals(result, "El vehicle va endavant->El vehicle va endarrere->El vehicle gira a l'esquerra")

    def test__giraesquerra__Camio(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user
            # Gràcies al osv.OsvInherits de ClasseCamio, podem accedir als mètodes mare de ClasseVehicle
            result = self.Camio.giraesquerra()

            self.assertEquals(result, "El vehicle gira a l'esquerra")

    def test__giraDreta__Camio(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            with self.assertRaises(AttributeError):
                # AttributeError: 'super' object has no attribute 'giraDreta'
                result = self.Camio.giraDreta()

    def test__parabrises__Camio(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user
            # Gràcies al osv.OsvInherits de ClasseCamio, podem accedir als mètodes mare
            #  en aquest cas de la ClasseCotxe, que ha extes el comportament de la ClasseVehicle
            result = self.Camio.parabrises()

            self.assertEquals(result, "Accionem el parabrises")

