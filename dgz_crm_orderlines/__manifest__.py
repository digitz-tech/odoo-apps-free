# -*- coding: utf-8 -*-
{
    'name': 'Crm Orderlines',
    'version': '16.0.1',
    'category': 'CRM',
    'author': 'Digitz Technologies',
    'website': 'www.digitztech.com',
    'summary': """ With this module, you can generate sales order lines directly from CRM. Clicking the 'New Quotation' button in CRM opens the corresponding sale order, preloaded with default order lines that were initially saved in CRM. """,
    'description': """ With this module, you can generate sales order lines directly from CRM. Clicking the 'New Quotation' button in CRM opens the corresponding sale order, preloaded with default order lines that were initially saved in CRM. """,
    'depends': ['crm', 'sale_crm', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'images': ['static/description/thumbnail.gif'],
}
