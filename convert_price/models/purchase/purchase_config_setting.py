# -*- coding: utf-8 -*-

from odoo import models
from odoo import fields
from odoo import api

class Setting(models.TransientModel):
    _inherit = 'purchase.config.settings'

    language_option = fields.Selection([('eng', 'English'),
                                       ('viet', 'Vietnamese')],
                                      required=True,
                                      default='eng',
                                      string="Language:")


    @api.multi
    def set_warning_option_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'purchase.config.settings', 'language_option', self.language_option)