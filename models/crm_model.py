# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError


class CustomCrm(models.Model):
    _inherit = 'crm.lead'

    contact_names = fields.Many2one('res.partner', 'Nombre del contacto')
    contact_email = fields.Char('Correo del contacto', related='contact_names.email_normalized', readonly=True)
    contact_function = fields.Char('Puesto de trabajo', related='contact_names.function', readonly=True)
    contact_phone = fields.Char('Teléfono del contacto', related='contact_names.phone', readonly=True)
    contact_mobil = fields.Char('Móvil del contacto', related='contact_names.mobile', readonly=True)

    
    def write(self, vals):
        last_stage_id = self.env['crm.stage'].search([('id', '=', self.stage_id.id)]).id
        next_stage_id = vals.get('stage_id')
        res = super(CustomCrm, self).write(vals)
        if next_stage_id:
            if last_stage_id == 2 and next_stage_id == 1:
                raise UserError(_('Movimiento inválido'))
            if last_stage_id == 3 and next_stage_id == 1:
                raise UserError(_('Movimiento inválido'))
            if last_stage_id == 1 and next_stage_id == 3:
                raise UserError(_('Movimiento inválido'))
            if last_stage_id in (1, 2, 5) and next_stage_id == 4:
                raise UserError(_('Movimiento inválido'))
            if last_stage_id == 4 and next_stage_id != 4:
                raise UserError(_('Movimiento inválido, una oportunadad ganada no puede cambiar de etapa'))
            if last_stage_id == 6 and next_stage_id != 6:
                raise UserError(_('Movimiento inválido, una oportunadad perdida no puede cambiar de etapa, en su lugar cree una nueva'))
            if last_stage_id == 7 and next_stage_id != 7:
                raise UserError(_('Movimiento inválido, una oportunadad cancelada no puede cambiar de etapa, en su lugar cree una nueva'))
        return res

