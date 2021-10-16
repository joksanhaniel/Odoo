# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Cursos'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()


    responsable_id = fields.Many2one('res.users', ondelete='set null', string="Responsable", index=True)
    session_id = fields.One2many('open_academy.session', 'course_id', string="Sessions")

    
    
    