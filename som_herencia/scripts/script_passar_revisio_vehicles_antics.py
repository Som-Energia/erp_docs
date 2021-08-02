from destral import testing
from destral.transaction import Transaction
from destral.patch import PatchNewCursors
import time
import random
from datetime import datetime
import dbconfig
from erppeek import Client as Client;

def passar_revisio_antics(): 
    c = Client(**dbconfig.erppeek)
    grupVehicle = c.ClasseVehicle.search([('data_compra','<','1990-01-01')])
    wiz = c.WizardPassarRevisio.create({'data_revisio': '2000-12-12'}, context={'active_id': grupVehicle[0], 'active_ids': grupVehicle})
    wiz.passar_revisio()



if  __name__ == '__main__':
    print("Executant passar_revisio_antics")
    passar_revisio_antics()






