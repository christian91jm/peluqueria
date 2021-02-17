#fechaVenta = fields.Date(string="Fecha", default=lambda self: datetime.today())
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime
from time import time

class facturas_model(models.Model):
    _name = 'peluqueria.facturas_model'
    _description = 'modelo de facturas'
    
    
    ref = fields.Char(string="Referencia",readonly=True,index=True,default=lambda self: str(int(time())))
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    cliente = fields.Many2one("peluqueria.clientes_model", string="Cliente")
    detalleP = fields.One2many("peluqueria.venta_producto_model", "facturas_id", string="Factura producto")
    detalleS = fields.One2many("peluqueria.venta_servicio_model", "facturas_id", string="Factura servicio")
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('7','7'),('5','5'),('0','0')])
    total = fields.Float(string="Total", compute="_calc_iva", store=True)

    @api.depends('detalleP','detalleS')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.detalleP:
            suma+= i.productos_id.precio*i.cantidad
        for i in self.detalleS:
            suma+= i.servicios_id.precio
        self.base=suma

    @api.depends('iva','base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = ((self.base*int(self.iva))/100)+self.base

