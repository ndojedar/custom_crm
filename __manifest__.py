# -*- coding: utf-8 -*-
{
    'name': "Custom CRM",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Adasoft",
    'website': "http://www.adasoft.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 
        'crm', 
        'crm_opportunity_product', 
        'base_automation',
        'sale', 
        'sale_management'
    ],

    # always loaded
    'data': [
        'data/automated.xml',
        # 'data/mail_data.xml',
        # 'security/ir.model.access.csv',
        'views/crm_lead_view.xml',
        'views/so_rev_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
