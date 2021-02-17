# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class productos_model(models.Model):
    _name = 'peluqueria.servicios_model'
    _description = 'Modelo de servicios'
    _order="name"

    _sql_constraints = [("sql_cons_check_id_servicio","UNIQUE(id_servicio)","Error en servicios. El id del servicio ya existe!"),]

    id_servicio = fields.Char(string="Id Servicio",readonly=True,index=True,default=lambda self: str(int(time())))
    name = fields.Char(string="Nombre", required=True)
    
    ventas = fields.One2many("peluqueria.venta_servicio_model","servicios_id",string="Pedidos Realizados",readonly=True)
    descripcion = fields.Char(string="Descripción")
    
    precio = fields.Float(string="Precio", required=True)
    