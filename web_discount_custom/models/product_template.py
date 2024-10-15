from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    price_sale_custom = fields.Float(string='Price', default=0.0)
    discount_percentage = fields.Float(string='Discount Percentage', default=0.0)
    discounted_price = fields.Float(string='Discounted Price', compute='_compute_discounted_price', store=True)
    discounted_price_tax_included = fields.Float(string='Discounted Price (Tax Included)', compute='_compute_discounted_price_tax_included', store=True)

    # When price_sale_custom or discount_percentage is changed, update list_price
    @api.onchange('price_sale_custom', 'discount_percentage')
    def _onchange_price_discount(self):
        for product in self:
            if product.discount_percentage > 0:
                discount_amount = product.price_sale_custom * (product.discount_percentage / 100)
                product.list_price = product.price_sale_custom - discount_amount  # Update list_price based on custom price and discount
            else:
                product.list_price = product.price_sale_custom  # No discount, list_price is the same as custom price

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage > 0:
                discount_amount = product.list_price * (product.discount_percentage / 100)
                product.discounted_price = product.list_price - discount_amount
            else:
                product.discounted_price = product.list_price

    @api.depends('discounted_price', 'taxes_id')
    def _compute_discounted_price_tax_included(self):
        for product in self:
            if product.discounted_price:
                taxes = product.taxes_id
                if taxes:
                    # Compute the tax amount based on the discounted price
                    tax_amount = sum(tax.compute_all(product.discounted_price)['total_included'] - product.discounted_price for tax in taxes)
                    product.discounted_price_tax_included = product.discounted_price + tax_amount
                else:
                    product.discounted_price_tax_included = product.discounted_price
            else:
                product.discounted_price_tax_included = 0.0
