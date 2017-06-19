# -*- coding: utf-8 -*-
# Copyright 2016 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Handle easily multiple variants on Purchases Orders',
    'summary': 'Handle the addition/removal of multiple variants from '
               'product template into the purchases order',
    'version': '10.0.1.0.0',
    'author': 'Tecnativa, Comunitea, '
              'Odoo Community Association (OCA)',
    'category': 'Purchase',
    'license': 'AGPL-3',
    'website': 'http://www.comunitea.com',
    'depends': [
        'purchase',
        'web_widget_x2many_2d_matrix',
    ],
    'demo': [],
    'data': [
        'wizard/purchase_manage_variant_view.xml',
        'views/purchase_order_view.xml',
    ],
    'installable': True,
}
