from odoo import api, fields, models, tools, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    name_arabic = fields.Char(string="Arabic Name")
    street_arabic = fields.Char(string="Arabic Street")
    street2_arabic = fields.Char(string="Arabic Street2")
    state_arabic = fields.Char(string="Arabic State")
    country_arabic = fields.Char(string="Arabic Country")
    city_arabic = fields.Char(string="Arabic City")
