from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float(string='discount')

    def action_open_discount_wizard(self):
        return {
            'name': 'Add Discount',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.extend.wizard',
            'view_mode': 'form',
            'target': 'new',
        }
