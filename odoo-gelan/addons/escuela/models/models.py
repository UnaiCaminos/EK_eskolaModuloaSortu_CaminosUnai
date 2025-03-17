# -*- coding: utf-8 -*-
from odoo import models, fields, api

class profesor(models.Model):
        _name = 'escuela.profesor'
        _description = 'profesor'
        name = fields.Char(string="Nombre", required=True)
        description = fields.Text(string="Descripcion")
        edad = fields.Integer(string="edad", required=True)
        fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
        saldo = fields.Float(string="saldo")
        estado = fields.Boolean(String="Estado del profesor")
        grado = fields.Selection(
                [
                      ('primaria', 'Primaria'),
                      ('basico', 'Basico'),
                ],
                string="Grado",
                default="primaria",
                required=True,
        )

      
