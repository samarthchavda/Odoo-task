from odoo import models,fields,api

class Sale_Order_Line(models.Model):
    _inherit = "sale.order.line"

    @api.model_create_multi
    def create(self, vals_list):
        order_line = super().create(vals_list)
        today = fields.date.today()

        for order in order_line:
            check_main_product = self.env['free.product'].search([
                ('main_product_id','=',order.product_id.id),
                ('start_date', '<=', today),
                ('end_date', '>=', today),
                # ('is_active','=',True),
            ], limit=1)

            if check_main_product:
                self.env["sale.order.line"].create({
                    "order_id": order.order_id.id,
                    "product_id": check_main_product.free_product_id.id,
                    "price_unit": 0.0,
                })

        return order_line