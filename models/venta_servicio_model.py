# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class venta_servicio_model(models.Model):
    _name = 'peluqueria.venta_servicio_model'
    _description = 'Modelo de ventas de servicio'
  
    facturas_id = fields.Many2one("peluqueria.facturas_model", "Factura")
    servicios_id = fields.Many2one("peluqueria.servicios_model", required=True)
    
    