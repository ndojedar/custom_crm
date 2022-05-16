
from odoo import _, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    active = fields.Boolean(default=True)

    def toggle_active(self):
        if self.filtered(lambda so: so.state not in ["cancel"] and so.active):
            raise UserError(_("Solo se pueden archivar pedidos 'Cancelados'"))
        return super().toggle_active()



#     def _order_revised_count(self):
#         for rec in self:
#             order_revised_count = self.search([('parent_saleorder_id', '=', rec.id)])
#             rec.so_revised_count = len(order_revised_count)

#     parent_saleorder_id = fields.Many2one('sale.order', 'Pedido padre', copy=False)
#     so_revised_count = fields.Integer('# de pedidos Revisados', compute='_order_revised_count', copy=False)
#     so_number = fields.Integer('SO Número', copy=False, default=1)
#     state = fields.Selection(selection_add=[('revised', 'Revisado')])


#     def so_revision_quote(self):
#         for rec in self:
#             if not rec.origin:
#                 origin_name = rec.name
#                 rec.origin = rec.name
#             else:
#                 origin_name = rec.origin

#             vals = {
#                 'name': 'RSO' + str(rec.so_number) + "_" + origin_name,
#                 'state': 'revised',
#                 'parent_saleorder_id': rec.id
#             }
#             rec.copy(default=vals)
#             rec.state = 'draft'
#             rec.so_number += 1