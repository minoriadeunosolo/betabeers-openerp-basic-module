# -*- encoding: utf-8 -*-
##################################################################################
#
#    Copyright (C) Betabeers
#
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

from openerp.osv import orm, fields

class res_betabeerspartner(orm.Model):
    _inherit = 'res.partner'
    _columns={ 'adiccion': fields.char('Adicciones',size=30),
               'date_clean': fields.date('Fecha Desintoxicación'),
               'observaciones': fields.text('Observaciones'),
               'speeches': fields.many2many(
                                   'betabeers.speech',
                                   'partner_speech_rel',
                                   'partner_id',
                                   'speech_id',
                                   'Charlas')
                }

class betabeers_charla(orm.Model):
            _name = 'betabeers.speech'
            _description = 'Charla Betabeers'
            _columns = { 'name': fields.char('Nombre charla', size=64, required=True, translate=True),
                         'description': fields.text('Descripcion Corta'),
                         'date_speech': fields.date('Fecha charla', required=True),
                         'author': fields.many2one('res.partner','Autor'),
                       }
