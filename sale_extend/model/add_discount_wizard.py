from odoo import models, fields

class AddDiscountWizard(models.TransientModel):
    _name = 'sale.extend.wizard'
    _description = 'Add Discount Wizard'

    discount_number = fields.Float(string="discount", required=True)

    def action_apply_discount(self):
        active_id = self.env.context.get('active_id')
        order = self.env['sale.order'].browse(active_id)

        for line in order.order_line:
            if line.product_id:
                line.discount = self.discount_number

        discount_product = self.env['product.product'].search([('name', '=','discount')])

        if not discount_product:
            self.env['sale.order.line'].create({
                'order_id': order.id,
                'product_id': discount_product.id,
                'name': discount_product.name,
            })