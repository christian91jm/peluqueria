# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class compras_model(models.Model):
    _name = 'peluqueria.compras_model'
    _description = 'Modelo de compras'
  
    _sql_constraints = [("sql_cons_check_id_compra","UNIQUE(id_compra)","Error en compras. El id de la compra ya existe!"),]

    id_compra = fields.Char(string="Id Compra",readonly=True,index=True,default=lambda self: str(int(time())))
    producto = fields.Many2one("peluqueria.productos_model", required=True)
    empleado = fields.Many2one("peluqueria.empleados_model", required=True)
    descripcion = fields.Char(string="Descripción Opcional")
    cantidad = fields.Integer(string="Cantidad", required=True, size=9)
    fechaPedido = fields.Date(string="Fecha", default=lambda self: datetime.today())
    total = fields.Float(string="Total", compute='calcula_precio', store=True)
    active = fields.Boolean(readonly=True, default=True)
    

    def actualizaStock(self):
          productos = self.search([("active","=","True")])
          for rec in productos:
               rec.producto.stock += rec.cantidad
               rec.active=False

    @api.depends('producto')
    def calcula_precio(self):
        self.total = self.producto.precio * self.cantidad