# som_herencia
Repositori per practicar com funciona l'herència a OpenERP / Odoo

## Testing
```bash
dodestral -m som_herencia --no-requirements
```

## Herència
![Inheritance diagram](img/inheritance_methods1.png)
### Class Inheritance
Per afegir/canviar el comportament a una classe. La fem servir per canviar mòduls existents a OpenERP
```bash
class ClasseVehicle(osv.osv):
  _name = 'classe.vehicle'

class ClasseVehicleHeredada(osv.osv):
  _name = 'classe.vehicle'
  _inherit = 'classe.vehicle'
```
Es pot accedir als camps i mètodes de la classe mare. No crea cap altra taula.

### Prototyping Inheritance
Per afegir/canviar el comportament a una classe.
```bash
class ClasseVehicle(osv.osv):
  _name = 'classe.vehicle'

class ClasseVehicleHeredada(osv.osv):
  _name = 'classe.vehicle.heredada'
  _inherit = 'classe.vehicle'
```
Es pot accedir als camps i mètodes de la classe mare. Crea una altra taula, copiant els camps de la classe mare a la nova taula i els registres de les dues taules són independents.

### Delegation Inheritance
```bash
class ClasseVehicle(osv.osv):
  _name = 'classe.vehicle'
_columns = {
  'matricula': fields.char("Matricula", size=10, required=False, unique=True,
  help="Matricula del vehicle",)
}

# No es pot accedir als mètodes mare
class ClasseVehicleHeredada(osv.osv):
  _name = 'classe.vehicle.heredada'
  _inherits = OrderedDict([('classe.vehicle', 'matricula')])
  _columns = {
    'matricula':fields.many2one('classe.vehicle','matricula',required=True),
    }

#Es pot accedir als mètodes mare
class ClasseVehicleHeredada(osv.OsvInherits):
  _name = 'classe.vehicle.heredada'
  _inherits = OrderedDict([('classe.vehicle', 'matricula')])
  _columns = {
    'matricula':fields.many2one('classe.vehicle','matricula',required=True),
    }
```
Es pot accedir als camps però no als mètodes de la classe mare. Crea una altra taula i els registres estan vinculats.

https://openerp-server.readthedocs.io/en/latest/03_module_dev_02.html?highlight=inherit#object-inheritance-inherit

## Model de dades
Per veure el model de dades que es crea podeu veure com queden les taules quan es carreguen les dades de demo
[Model de dades demo](demo/README.md)
