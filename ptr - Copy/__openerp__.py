
{
    'name' : "Patrimoines",
    'version' : '1.0',
    'author' : 'Mohamed Chatei',
    'category' : 'ENSAH ERP',
	'sequence' :1,
    'description' : """
	
Module basique de démenstration de gestion du patrimoine.
======================================================

Ce module couvre les éléments suivants:
------------------------------------------------------
    * Gestion des laucaux
    * Gestion des departements
	* Gestion des inventaires de l Ecole
   """,
    'website': 'http://www.monsite.ma',
    'images' : [''],
    'depends' : ['base'],
    'data': ['ptr_etablissement_view.xml',
	         'ptr_inv_view.xml',
			  'ptr_departement_view.xml',
			  'ptr_local_view.xml',
			  'ptr_responsable_view.xml',
			  'ptr_categoriepersonnel_view.xml',
			  'ptr_typeptrgeo_view.xml'],
    'update_xml': [ ],
    'js': [],
    'qweb' : [],
    'css':[''],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
