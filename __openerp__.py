# -*- coding: utf-8 -*-

######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

{
    'name': 'Modulo Ejemplo Betabeers',
    'version': '1.1',
	'author': 'Miguel Ángel Rico',
	'summary': 'Ejemplo de modulo para betabeers Malaga',
	'description': """
Ejemplo de creación de un modulo simple en OpenERP 7.0
Contact: betabeers
        """,
    'maintainer': 'Betabeers',
    'website': '',
    "images" : [],
    'depends': ['base'],
    'init_xml': [ 'views/mod_view.xml'],
    'demo_xml': [],
    'update_xml': ['views/mod_view.xml'],
     'images': [],
    'active': True,
    'installable': True,
    'application':True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
