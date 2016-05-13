from openerp.osv import osv, fields


class StockMove(osv.osv):
    _inherit = 'stock.move'


    def action_confirm(self, cr, uid, ids, context=None):
        for move in self.browse(cr, uid, ids, context=context):
	    if move.procurement_id.name == 'Phantom BOM':
		move.procure_method = 'make_to_stock'
	    elif move.procure_method == 'make_to_order' and round(move.availability, 2) >= round(move.product_qty, 2):
	        move.procure_method = 'make_to_stock'

	return super(StockMove, self).action_confirm(cr, uid, ids, context)
