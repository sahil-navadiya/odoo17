{
    'name': 'Website Product Discount',
    'version': '17.0.1',
    'summary': 'Apply discounts to products on the eCommerce website',
    'description': """
        Apply discounts to products on the eCommerce website.
    """,
    'category': 'Website',
    'author': 'Sahil Navadiya',
    'maintainer': 'Sahil Navadiya',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'website_sale',
        'product',
        'base',
        'website',
        'sale_product_configurator',
    ],
    'data': [
        'views/product_template_views.xml',  # Backend view modification
        'views/cart_templates.xml',          # Cart and checkout templates (if modified)
        'views/website_product_template.xml', 
    ],
    'installable': True,
    
    'application': False,
    'auto_install': False,
}
