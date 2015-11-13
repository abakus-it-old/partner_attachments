from openerp import models, fields

class PartnerWithAttachment(models.Model):
    _inherit = 'res.partner'
    
    attachments_ids = fields.Many2many('ir.attachment', string="Attachments")