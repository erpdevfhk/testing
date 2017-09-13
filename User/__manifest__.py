#User account module for system access
#Created By:
#Farhan Javed
#07-09-2017
{
    'name':"User",
    'Category':'Test',
    'version' : '1.0',
    'author': 'Farhan Javed',
    'depends' : ['base'],
    'website' : 'www.user.com',
    'description' : """
        User module which stores information regarding
        users who access the system. These can be both employees
        and customers.
    """,
    'data': [
        'views/menu.xml',
        'views/user.xml'
    ],
}