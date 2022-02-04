# -*- coding: utf-8 -*-
# from odoo import http


# class Demo/demoPrint(http.Controller):
#     @http.route('/demo/demo_print/demo/demo_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo/demo_print/demo/demo_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo/demo_print.listing', {
#             'root': '/demo/demo_print/demo/demo_print',
#             'objects': http.request.env['demo/demo_print.demo/demo_print'].search([]),
#         })

#     @http.route('/demo/demo_print/demo/demo_print/objects/<model("demo/demo_print.demo/demo_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo/demo_print.object', {
#             'object': obj
#         })
