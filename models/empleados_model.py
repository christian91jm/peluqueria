# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time
from time import time

class empleados_model(models.Model):
    _name = 'peluqueria.empleados_model'
    _description = 'Modelo de empleados'
    _order="name"
    _sql_constraints = [("sql_cons_check_dni_empleado","UNIQUE(dni)","Error en empleado. El dni del empleado ya existe!"),
                         ("sql_cons_check_id_empleado","UNIQUE(id_empleado)","Error en empleado. El id  del empleado ya existe!"),]

    id_empleado = fields.Char(string="Id Empleado",readonly=True,index=True,default=lambda self: str(int(time())))
    dni = fields.Char(string="DNI", required=True, size=9, index=True)
    foto = fields.Binary(string="Foto", required=False)
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Char(string="Teléfono", required=True, size=9)
    email = fields.Char(string="Email", required=True)
    fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
    salarioBase = fields.Float(string="Sueldo Base")
    compras = fields.One2many("peluqueria.compras_model","empleado",string="Pedidos Realizados",readonly=True)

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 carácteres!")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")
     
     
     
     