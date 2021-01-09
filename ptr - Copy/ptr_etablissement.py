from openerp.osv import osv,fields
import openerp
class ptr_etablissement(osv.osv):
    _name='ptr.etablissement'
    _columns={
        'name': fields.char('Nom', size=128),
        'code': fields.char('Code', size=64),
        'adresse': fields.char('Adresse'),
        'fixe': fields.char('Telephone fixe'),
        'faxe': fields.char('Faxe'),
		'president': fields.char('President', size=64),
		'capacite': fields.float('Capacite'),
		'departement_ids':fields.one2many('ptr.departement','id_etablissement',string='Departement'),
		'inv_ids':fields.one2many('ptr.inv','id_inv',string='Inventaire')
			}
ptr_etablissement()