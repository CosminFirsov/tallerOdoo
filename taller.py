# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
class taller_propietarios(osv.osv):
    _name = 'taller.propietarios'
    _columns = {
    'name': fields.char('Nombre', size=150, requerided=True),
    'telefono': fields.char('Telefono', size=150, requerided=True),
    'direccion': fields.char('Direccion', size=150),
    'coches': fields.one2many('taller.coches', 'propietario', 'coches')
    }

taller_propietarios()

class taller_coches(osv.osv):
    _name='taller.coches'
    _columns = {
    'tipo': fields.selection((('0','Coche'),('1','Motos'),('2','Otros')),'Tipo'),
    'marca': fields.char('Marca', size=50),
    'modelo': fields.char('Modelo', size=50),
    'color': fields.char('Color', size=20),
    'puertas': fields.integer('Nº de Puertas'),
    'matricula': fields.char('Matricula',size=10,required=True),
    'fecmat': fields.date('Fecha de Matriculacion'),
    'kilometraje': fields.float('Kilometros', digits=(8,3)),
    'longitud': fields.integer('Longitud (mm)'),
    'altura': fields.integer('Altura (mm)'),
    'anchura': fields.integer('Anchura (mm)'),
    'capacidad': fields.integer('Capacidad del Maletero (m3)'),
    'numbastidor': fields.char('Nº Bastidor', size=20),
    'cilindrada': fields.integer('Cilindrada (cc)'),
    'numcilindros': fields.integer('Nº de cilindros'),
    'potenciafiscal': fields.float('Potencia fiscal (cv)', digits=(4,2)),
    'potencia': fields.float('Potencia', digits=(4,2)),
    'combustible': fields.selection((('0','Gasolina'),('1','Diesel')),'Combustible'),
    'gastomedio': fields.float('Gasto medio (100km)', digits=(4,2)),
    'velocidad': fields.integer('Velocidad'),
    'comentarios': fields.text('Comentarios'),
    'terminado': fields.boolean('Terminado'),
    'itv': fields.selection((('0','Pasada'),('1','No pasada'), ('2','No necesario')),'ITV'),
    'propietario': fields.many2one('taller.propietarios','Propietario',ondelete='cascade')
    }

taller_coches()
