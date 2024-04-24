# -*- coding: utf-8 -*-
from osv import osv


class ModelName(osv.osv):
    _name = 'model.name'
    _description = 'Model Name'

    _columns = {
        'name': fields.char("Nom", size=128),
        'active': fields.boolean('Active'),
        'create_uid': fields.many2one('res.users', 'Usuari creador', readonly=1, select=2),
        'partner_id': fields.many2one('res.partner', 'Partner',
                                      select=True, change_default=True, readonly=True,
                                      required=True, states={'draft': [('readonly', False)]}),

    _order = "id desc"

    _defaults = {
        'active': lambda *a: True,
    }


ModelName()
