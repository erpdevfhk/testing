"""
Employees.py file containing the data fields for the employees class
Used to collect all the information regarding all the employees in the company.
Created by: Farhan Javed - 12/09/2017
"""

from odoo import models, fields, api, _

class employees(models.Model):
    _name="order.employees"

    employee_id = fields.Integer(required="True",string="Employee ID")
    employee_name = fields.Char(required="True", string="Employee Name")
    employee_dob = fields.Date(required="True", string="Employee Date Of Birth")
    employee_passport_no = fields.Text(required="True", string="Employee Passport Number")
    employee_visa_no = fields.Text(required="True", string="Employee Visa Number")
    employee_sex = fields.Selection([('m','Male'),('f','Female')],string="Employee Sex")
    employee_contact_no = fields.Integer(required="True", string="Employee Contact Number")
    employee_address = fields.Text(required="True", string="Employee Address")
    employee_designation = fields.Char(required="True", string="Employee Designation")
    employee_driving_license_no=fields.Text(string="Employee Driving License") # Only for the employees who will driver vehicles
    #employee_dept_id = fields.Integer(required="True", string="Employee Department ID")
