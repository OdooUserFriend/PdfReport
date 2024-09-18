# -*- coding: utf-8 -*-
{
    'name': 'Base Report',
    'version': '13.0.1.0',
    'category': 'Reports',
    'author': 'Febno',
    'website': "",
    'description': """
        -Invoice and sales reports.
    """,
    'depends': ['base','account','sale',],
    'data': [
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'reports/custom_invoice.xml',
        'reports/report_iv.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}