# -*- coding: utf-8 -*-
from osv import osv, fields


class WizardPassarRevisio(osv.osv_memory):
    _name = 'wizard.passar.revisio'

    def passar_revisio(self, cursor, uid, id, context=None):
        if not context:
            return False
        active_id = context.get('active_id')

        #carregar el model
        Vehicle = self.pool.get('classe.vehicle')

        #cridar el passar revisio
        Vehicle.passar_revisio(cursor, uid, active_id)

        return True


        #vehicle_obj = Vehicle.browse(2)
        #vehicle_obj.passar_revisio()

WizardPassarRevisio()