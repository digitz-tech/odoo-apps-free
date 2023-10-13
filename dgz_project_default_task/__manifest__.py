# -*- coding: utf-8 -*-
{
    'name': 'Project Default Task',
    'version': '16.0.1',
    'sequence': 1,
    'website': 'https://digitztech.com',
    'category': 'Extra Tools',
    'summary': """This module serves the purpose of creating predefined task to project according to the category of the project.""",
    'description': """ This module serves the purpose of creating predefined task to project according to the category of the project. """,
    'author': 'Aravind',
    'depends': ['project'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/project_category.xml',
        'views/project.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/baner.gif'],
}
