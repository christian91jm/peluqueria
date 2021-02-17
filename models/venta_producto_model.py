# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class venta_producto_model(models.Model):
    _name = 'peluqueria.venta_producto_model'
    _description = 'Modelo de ventas de producto'
  
    facturas_id = fields.Many2one("peluqueria.facturas_model", "Factura")
    productos_id = fields.Many2one("peluqueria.productos_model", required=True)
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)
    


    
    