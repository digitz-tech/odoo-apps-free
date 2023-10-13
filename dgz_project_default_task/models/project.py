# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectUpdates(models.Model):
    _inherit = 'project.project'

    category_id = fields.Many2one('project.category', 'Category')

    @api.model_create_multi
    def create(self, values):
        result = super(ProjectUpdates, self).create(values)
        try:
            if result.category_id:
                if result.category_id.active and result.category_id.task_ids:
                    if result.category_id.stage_ids:
                        for stage in result.category_id.stage_ids:
                            stage.write({'project_ids': [(4, result.id)]})
                    for rec in reversed(result.category_id.task_ids):
                        if rec.user_ids:
                            user_ids = rec.user_ids.ids
                        elif result.category_id.user_ids:
                            user_ids = result.category_id.user_ids.ids
                        else:
                            user_ids = False
                        if rec.stage_id:
                            stage_id = rec.stage_id.id
                        elif result.category_id.stage_ids:
                            stage_id = result.category_id.stage_ids.ids[0]
                        else:
                            stage_id = False
                        task_dict = {'name': rec.name, 'description': rec.description, 'project_id': result.id,
                                     'user_ids': user_ids, 'stage_id': stage_id,'priority': '1' if rec.priority == '1' else '0' }
                        self.env['project.task'].sudo().create(task_dict)
        except Exception:
            pass
        return result
