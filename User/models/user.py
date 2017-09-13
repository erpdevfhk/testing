from odoo import models, fields, api, _

class Useruser(models.Model):
    _name = 'user.user'

    user_id = fields.Integer(required="True", string="User ID")
    password = fields.Char(required="True", string="Password")
    cutOffLimit = fields.Integer(required="True", string="Cut Off Limit")