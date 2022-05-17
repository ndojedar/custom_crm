# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning

class CrmMessageWizard(models.TransientModel):
    _name = "crm.message.wizard"
    _description = "Mensajes personalizados"


    message = fields.Text(string="Mensaje")


    @api.model
    def generated_message(self, message, name='AVISO!'):
        res = self.create({'text': message})
        return {
            'name'     : name,
            'type'     : 'ir.actions.act_window',
            'res_model': 'crm.message.wizard',
            'view_mode': 'form',
            'target'   : 'new',
            'res_id'   : res.id,
        }
