#Order Module for processing ATM Replenishment Orders
#Created BY: Farhan Javed
#12/09/2017
{
    'name':'order',
    'Category' : 'Deployment',
    'version' : '1.0',
    'author' : 'Farhan Javed',
    'depends' : ['base'],
    'website' : 'www.website.com',
    'description' : """
            Order module which is currently being used for processing
            ATM Replenishment orders by the banks.
    """,
    'data' : [
        'views/menu.xml',
        'views/customers.xml',
        'views/employees.xml',
        'views/branch.xml',
    ],
}