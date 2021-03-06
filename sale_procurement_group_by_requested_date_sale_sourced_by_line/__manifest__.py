# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Group procurements by source wh and requested date",
    "summary": "Integrates sale_source_by_line and sale procurement group",
    "version": "10.0.1.0.0",
    "category": "Sales Management",
    'website': "https://github.com/OCA/sale-workflow",
    "author": "Eficent , "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": [
        "sale_sourced_by_line",
        "sale_procurement_group_by_requested_date",
    ],
    "installable": True,
    "auto_install": True,
}
