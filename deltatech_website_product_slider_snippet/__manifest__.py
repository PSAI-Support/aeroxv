# ©  2008-2021 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details
{
    "name": "eCommerce Product Slider",
    "category": "Website",
    "summary": "eCommerce extension",
    "version": "15.0.1.0.0",
    "author": "Terrabit, Dorin Hongu",
    "license": "AGPL-3",
    "website": "https://www.terrabit.ro",
    "depends": ["website_sale", "deltatech_product_list"],
    "data": ["views/templates.xml", "views/snippets.xml"],
    "images": ["static/description/main_screenshot.png"],
    "installable": True,
    "qweb": ["static/src/xml/*.xml"],
    "development_status": "Mature",
    "maintainers": ["dhongu"],
    "assets": {
        "website.assets_wysiwyg": [
            "/deltatech_website_product_slider_snippet/static/src/js/website_products_slider_editor.js"
        ],
    },
}
