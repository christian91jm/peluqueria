# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class productos_model(models.Model):
    _name = 'peluqueria.productos_model'
    _description = 'Modelo de productos'
    _order="name"

    _sql_constraints = [("sql_cons_check_id_producto","UNIQUE(id_producto)","Error en productos. El id del producto ya existe!"),]

    id_producto = fields.Char(string="Id Producto",readonly=True,index=True,default=lambda self: str(int(time())))
    name = fields.Char(string="Nombre", required=True)
    compras = fields.One2many("peluqueria.compras_model","producto",string="Pedidos Realizados",readonly=True)
    ventas = fields.One2many("peluqueria.venta_producto_model","productos_id",string="Pedidos Realizados",readonly=True)
    descripcion = fields.Char(string="Descripción")
    stock = fields.Integer(string="Stock", readonly=True)
    precio = fields.Float(string="Precio unidad", required=True)
    

    #cambiar id por lambda self: str(int(time()) por ejemplo