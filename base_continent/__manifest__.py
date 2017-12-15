# -*- coding: utf-8 -*-
# © 2014-2016 Camptocamp SA (Author: Romain Deheele)
# © 2017 senseFly, Amaris (Author: Quentin Theuret)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Continent management',
    'version': '10.0.1.0.1',
    'depends': [
        'base',
        'sales_team',
    ],
    'author': "Camptocamp,senseFly,Amaris,Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'description': """
This module introduces continent management.
============================================
Links continents to countries,
adds continent field on partner form
""",
    'category': 'Generic Modules/Base',
    'data': [
        'base_continent_view.xml',
        'base_continent_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
