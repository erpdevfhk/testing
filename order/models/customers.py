"""
Customers.py file containing the data fields for the customer class
Used to store information about all the customers that the company is going to serve.
Created by: Farhan Javed - 11/09/2017
"""
from odoo import models, fields, api, _

class ordercustomers(models.Model):
    _name='order.customers'

    customer_id=fields.Integer(required="True", string="Customer ID")
    customer_name = fields.Char(required="True", string="Customer Name")
    customer_type = fields.Char(required="True", string="Customer Type")
    headquarter_loc=fields.Text(required="True", string="HeadQuarter Location")
    headquarter_phone_no=fields.Integer(string="HeadQuarter Phone Number")