# -*- coding: utf-8 -*-

{
    'name': 'Module name',
    'description': 'Module summary',
    'version': '0.1',
    'category': 'Som Energia module',
    'website': 'https://github.com/Som-Energia/openerp-som-addons',
    'author': 'Som Energia SCCL',
    'license': 'AGPL-3',
    'active': False,
    'installable': True,
    'depends': [
        'base_extended_som',
    ],
    'init_xml': [],
    'update_xml': [
        'views/assets.xml',
        'views/report_name.xml',
        'views/res_partner_view.xml',
        'wizard/wizard_model_view.xml',
        'security/some_model_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [
        'demo/res_partner_demo.xml',
    ],
}
