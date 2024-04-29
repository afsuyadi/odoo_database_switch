# -*- coding: utf-8 -*-
# from odoo import http


# class BmbDev(http.Controller):
#     @http.route('/bmb_dev/bmb_dev', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bmb_dev/bmb_dev/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bmb_dev.listing', {
#             'root': '/bmb_dev/bmb_dev',
#             'objects': http.request.env['bmb_dev.bmb_dev'].search([]),
#         })

#     @http.route('/bmb_dev/bmb_dev/objects/<model("bmb_dev.bmb_dev"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bmb_dev.object', {
#             'object': obj
#         })
