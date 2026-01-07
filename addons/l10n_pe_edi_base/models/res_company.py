#######################################################################################
#
#    Copyright (C) 2019-TODAY OPeru.
#    Author      :  Grupo Odoo S.A.C. (<http://www.operu.pe>)
#
#    This program is copyright property of the author mentioned above.
#    You can`t redistribute it and/or modify it.
#
#######################################################################################

from odoo import api,fields, models

class Company(models.Model):
    _inherit = "res.company"

    l10n_pe_edi_send_invoice = fields.Boolean(string="Send E-Documents to PSE/OSE")
    l10n_pe_edi_ose_id = fields.Many2one(
        'l10n_pe_edi.supplier',
        string='PSE / OSE Provider',
        help='Electronic invoicing provider (PSE/OSE)'
    )
    l10n_pe_edi_send_invoice_interval_unit = fields.Selection(
        selection=[("hourly", "Hourly"), ("daily", "Daily")],
        default="daily",
        string="Interval Unit for sending",
    )
    l10n_pe_edi_send_invoice_next_execution_date = fields.Datetime(
        string="Next Execution", default=fields.Datetime.now()
    )
    l10n_pe_service_token = fields.Char("Service token")
    l10n_pe_edi_send_picking = fields.Boolean(string="Send E-Pickings to PSE/OSE")

    l10n_pe_edi_picking_default_catalog_18_id = fields.Many2one(
        comodel_name="l10n_pe_edi.catalog.18", string="Default Transport Type"
    )
    l10n_pe_edi_picking_default_carrier_id = fields.Many2one(
        comodel_name="res.partner", string="Default Carrier"
    )
    l10n_pe_edi_picking_default_driver_id = fields.Many2one(
        comodel_name="res.partner", string="Default Driver"
    )
    l10n_pe_edi_picking_default_auto_field_arrival_point = fields.Boolean(
        string="Default Auto Arrival Point",
        default=True
    )
    l10n_pe_enterprise_edi_installed = fields.Boolean(
        string="Enterprise EDI Installed",
        compute='_compute_l10n_pe_enterprise_edi_installed',
        store=True
    )
    l10n_pe_edi_pos_installed = fields.Boolean(
        string="POS EDI Installed",
        compute='_compute_l10n_pe_edi_pos_installed',
        store=True,
    )

    @api.depends('country_id')
    def _compute_l10n_pe_enterprise_edi_installed(self):
        """Check if Enterprise EDI module is installed"""
        module = self.env['ir.module.module'].search(
            [('name', '=', 'l10n_pe_edi'), ('state', '=', 'installed')], 
            limit=1
        )
        edi_installed = bool(module)
        
        for record in self:
            record.l10n_pe_enterprise_edi_installed = (
                edi_installed and record.country_id.code == 'PE'
            )
    
    @api.depends('country_id')
    def _compute_l10n_pe_edi_pos_installed(self):
        """Check if l10n_pe_edi_pos module is installed"""
        module = self.env['ir.module.module'].search(
            [('name', '=', 'l10n_pe_edi_pos'), ('state', '=', 'installed')],
            limit=1
        )
        pos_installed = bool(module)
        for record in self:
            record.l10n_pe_edi_pos_installed = (
                pos_installed and record.country_id.code == 'PE'
            )

    @api.model
    def _cron_update_enterprise_edi_flag(self):
        """Recalcula el flag de Enterprise EDI para todas las compañías."""
        companies = self.sudo().search([])
        companies._compute_l10n_pe_enterprise_edi_installed()

    @api.model
    def _cron_update_pos_edi_flag(self):
        """Recalcula el flag de POS EDI para todas las compañías."""
        companies = self.sudo().search([])
        companies._compute_l10n_pe_edi_pos_installed()