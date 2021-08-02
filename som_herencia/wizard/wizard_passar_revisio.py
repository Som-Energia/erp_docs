# -*- coding: utf-8 -*-
from osv import osv, fields


class WizardPassarRevisio(osv.osv_memory):
    _name = 'wizard.passar.revisio'

    def passar_revisio(self, cursor, uid, ids, context=None):
        if not context:
            return False

        #Controlar tema ids[]
        if not isinstance(ids, (tuple, list)):
            ids = [ids]

        wiz = self.browse(cursor, uid, ids[0], context=context)
        data = wiz.data_revisio

        active_id = context.get('active_id')
        active_ids = context.get('active_ids')
        #import pudb;pu.db
        #carregar el model
        Vehicle = self.pool.get('classe.vehicle')

        #cridar el passar revisio
        for n in active_ids:
            Vehicle.passarRevisio(cursor, uid, n, data, context)

        return {'type': 'ir.actions.act_window_close'}


        #vehicle_obj = Vehicle.browse(2)
        #vehicle_obj.passar_revisio()

    _columns = {
        'data_revisio': fields.date(
                       "Data revisió", required=False,
                        help = "Quin dia es va fer la ultima revisio",)
    }

WizardPassarRevisio()