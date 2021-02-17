# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class clientes_model(models.Model):
    _name = 'peluqueria.clientes_model'
    _description = 'Modelo de clientes'
    _order="name"
    _sql_constraints = [("sql_cons_check_id_cliente","UNIQUE(id_cliente)","Error en cliente. El id del cliente ya existe!"),]

    id_cliente = fields.Char(string="Id Empleado",readonly=True,index=True,default=lambda self: str(int(time())))
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Integer(string="Teléfono", required=True, size=9)
    email = fields.Char(string="Email", required=True)
    fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
    facturas = fields.One2many("peluqueria.facturas_model", "cliente", string="Facturas")
    #añadir un numero de socio desde herencia
   