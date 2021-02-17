# -*- coding: utf-8 -*-
# from odoo import http


# class Peluqueria(http.Controller):
#     @http.route('/peluqueria/peluqueria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/peluqueria/peluqueria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('peluqueria.listing', {
#             'root': '/peluqueria/peluqueria',
#             'objects': http.request.env['peluqueria.peluqueria'].search([]),
#         })

#     @http.route('/peluqueria/peluqueria/objects/<model("peluqueria.peluqueria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('peluqueria.object', {
#             'object': obj
#         })
