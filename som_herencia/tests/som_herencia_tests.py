# -*- coding: utf-8 -*-
from destral import testing
from destral.transaction import Transaction
from destral.patch import PatchNewCursors
import netsvc
import time
import random

class VehicleTests(testing.OOTestCase):
    def setUp(self):
        self.pool = self.openerp.pool
        self.Vehicle = self.pool.get('classe.vehicle')
        self.Moto = self.pool.get('classe.moto')
        self.Cotxe = self.pool.get('classe.vehicle')
        self.Camio = self.pool.get('classe.camio')
        self.Autocar = self.pool.get('classe.autocar')

    def tearDown(self):
        #self.txn.stop()
        pass

    def test__ferHoTot_Vehicle(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Vehicle.ferhotot()

            self.assertEquals(result, "El vehicle va endavant->El vehicle va endarrere->El vehicle gira a l'esquerra") 

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

            self.assertEquals(result, "El vehicle va endavant->El vehicle va endarrere->El vehicle gira a l'esquerra")

    def test__ferCaballet__Moto(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            result = self.Moto.fercaballet()

            self.assertEquals(result, "Fem el caballet")

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

    def test__giraVolantEsquerra__Autocar(self):
        """
        Checks if when state changed, everithing works
        :return:
        """
        with Transaction().start(self.database) as txn:
            cursor = txn.cursor
            uid = txn.user

            with self.assertRaises(AttributeError):
                #El mètode self.giraesquerra() de la classe Vehicle no és accessible des de Autocar
                result = self.Autocar.giraVolantEsquerra()

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

            result = self.Camio.giraVolantEsquerra()

            self.assertEquals(result, "Gira el volant del Camió a l'esquerra -> El vehicle gira a l'esquerra")

