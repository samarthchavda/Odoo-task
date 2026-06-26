from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FreeProduct(models.Model):
    _name = 'free.product'

    main_product_id = fields.Many2one(
        'product.product',
        string='Main Product',
        required=True,
    )

    free_product_id = fields.Many2one(
        'product.product',
        string='Free Product',
        required=True,
    )
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ],default='draft')

    start_date = fields.Date(string='Start Date',default=fields.Date.today)
    end_date = fields.Date(string='End Date',required=True)

    is_active = fields.Boolean(string='Active',default=False,compute='_compute_is_active',store=True)

    @api.constrains('start_date', 'end_date')
    def _check_free_product_active(self):
        for rec in self:
            if rec.end_date <= rec.start_date :
                raise ValidationError("End Date cannot be earlier than Start Date.")

    # @api.depends('start_date', 'end_date')
    # def _compute_is_active(self):
    #     today = fields.Date.today()
    #     if self.start_date <= today <= self.end_date:
    #         self.is_active = True
    #     else:
    #         self.is_active = False