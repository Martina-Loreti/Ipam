# -*- coding: utf-8 -*-
# from odoo import http


# class NomeProva(http.Controller):
#     @http.route('/nome_prova/nome_prova/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nome_prova/nome_prova/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nome_prova.listing', {
#             'root': '/nome_prova/nome_prova',
#             'objects': http.request.env['nome_prova.nome_prova'].search([]),
#         })

#     @http.route('/nome_prova/nome_prova/objects/<model("nome_prova.nome_prova"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nome_prova.object', {
#             'object': obj
#         })
