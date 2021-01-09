import openerp
from openerp import addons
from openerp.osv import osv,fields
from openerp import tools


class ptr_inv(osv.osv):
    _name='ptr.inv'
    _columns={
        'name': fields.char('Nom Inventaire', size=128),
        'date_inv_dec': fields.date('Date de declanchement'),
		'date_inv_ar': fields.date('Date d arret'),
		'duree': fields.float('Duree'),
		'id_inv':fields.many2one('ptr.etablissement', 'Etablissement', ondelete='cascade'),

			}
ptr_inv()