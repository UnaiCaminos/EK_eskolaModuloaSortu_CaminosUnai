# -*- coding: utf-8 -*-
from odoo import models, fields, api

class profesor(models.Model):
        _name = 'escuela.profesor'
        _description = 'Profesores'
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
        alumno = fields.One2many("escuela.alumno", inverse_name="profesor", string="Alumno")
        materia = fields.Many2many(
                comodel_name="escuela.materia",
                relation_name = "escuelas.materias",
                column1="escuela_id",
                column2="materia_id",
        )

class alumno(models.Model):
        _name = 'escuela.alumno'
        _description = 'Alumnos'
        name = fields.Char(string="Nombre", required=True)
        profesor = fields.Many2one("escuela.profesor")
        notas_id = fields.One2many("escuela.nota", "alumno_id", string="Notas")


class materia(models.Model):
        _name = 'escuela.materia'
        _description = 'Materias'
        name = fields.Char(string="Nombre", required=True)
        materia = fields.Many2many(
                comodel_name="escuela.profesor",
                relation_name = "escuelas.profesores",
                column1="materia_id",
                column2="escuela_id",
        )
        notas_ids = fields.One2many("escuela.nota", "materia_id", string="Notas")
        alumno_ids = fields.Many2many("escuela.alumno", string="Alumnos", compute="_compute_alumno_ids")

        @api.depends("notas_ids", "notas_ids.alumno_id")
        def _compute_alumno_ids(self):
                for materia in self:
                        materia.alumno_ids = materia.notas_ids.mapped("alumno_id")

class nota(models.Model):
        _name = 'escuela.nota'
        _description = 'Nota de alumno en materia'
        alumno_id = fields.Many2one("escuela.alumno", string="Alumno", required=True)
        materia_id = fields.Many2one("escuela.materia", string="materia", required=True)
        nota = fields.Integer(string="Nota")
        estado = fields.Char(string="Estado", compute="_compute_estado")
        
        @api.depends('nota')
        def _compute_estado(self):
                for record in self:
                        if record.nota >= 50:
                                record.estado = "Aprobado"
                        else:
                                record.estado = "Suspendido"