# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectCategory(models.Model):
    _name = 'project.category'

    name = fields.Char('Name')
    active = fields.Boolean('Active', default=True)
    user_ids = fields.Many2many('res.users', string='Assignees',help="Assign users to Task's, if there is no Assignees in the Task")
    stage_ids = fields.Many2many('project.task.type', string='Stages', help="Stages for the Task's")
    task_ids = fields.One2many('project.category.task', 'project_categ_id', 'Task')


class ProjectCategoryTask(models.Model):
    _name = 'project.category.task'

    name = fields.Char('Name', help='Name for the Task')
    priority = fields.Selection([('0','Low'),('1','High')])
    description = fields.Char('description', help='Description for the Task')
    user_ids = fields.Many2many('res.users', string='Assignees', help='Assign Specif Users')
    project_categ_id = fields.Many2one('project.category', 'Project Category')
    stage_id = fields.Many2one('project.task.type', 'Stage', help='High priority Stage')
