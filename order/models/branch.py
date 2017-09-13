"""
Branch.py file containing the data fields for the branch class
Each Customer will have at least one branch which will be served by the system.
Even if customer has one branch, that will be served as a branch.
Created by: Farhan Javed - 13/09/2017
"""
from odoo import models, fields,api,_

class branch(models.Model):
    _name="order.branch"

    branch_code=fields.Integer(required="True", string="Branch code")
    customer_id = fields.One2many('order.customers','customer_id',string="Customer ID")
    branch_address=fields.Text(required="True", string="Branch address")
    branch_phone_no=fields.Integer(required="True", string="Branch Phone No")
    # branch amount limit is the limit uptil which the amount of that branch inside the vaults is insured.
    branch_amount_limit=fields.Integer(required="True",string="Insured amount of the branch")
    # Branch Location Limit = The area around the branch in which the van is insured
    branch_location_limit=fields.Text(required="True", string="Insured perimeter around the branch")
    branch_maps_location=fields.Text(string="Maps Location of the branch") #used for geofencing