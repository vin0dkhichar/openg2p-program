from odoo import _, fields, models
from odoo.exceptions import ValidationError


class G2PCycleMembershipInherited(models.Model):
    _inherit = "g2p.cycle.membership"

    rank = fields.Integer(string="Rank", index=True)