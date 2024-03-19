# som_workflow

Mòdul per practicar com funcionen els *workflows* a OpenERP. En l'ERP, per exemple, els fem servir a la pòlissa o al PowerSMS.

## Workflows

Els *workflows* van associats a un model de l'ERP i ens permeten estructurar i gestionar el canvi entre diferents estats. Són un graf dirigit on els nodes es diuen *activities* i els vèrtexs *transitions*.

Es defineixen en un XML i estan compostos de:

### Workflow (defineix un nou *workflow*)

```
<record id="wkf_example" model="workflow">
    <field name="name">Example model workflow</field>
    <field name="osv">example.model</field>
    <field name="on_create">True</field>
</record>
```

Amb `<field name="on_create">True</field>` especifiquem que s'ha de crear una instància del *workflow* per cada registre del model que creem.

### Activites (nodes)

```
<record id="act_draft" model="workflow.activity">
    <field name="wkf_id" ref="wkf_example"/>
    <field name="flow_start">True</field>
    <field name="name">draft</field>
    <field name="kind">function</field>
    <field name="action">write({'state':'draft'})</field>
</record>
```

En les *activities* podem definir quina acció es farà al canviar a cada una d'elles (`<field name="action">write({'state':'draft'})</field>`). Podem introduir directament codi o cridar un mètode del model (automàticament es passa el `self`, `cursor`, `uid` i `context`).

D'altra banda, amb `<field name="flow_start">True</field>` especifiquem si és el node inicial.

### Transitions (vèrtexs)
```
<record id="trans_draft_open" model="workflow.transition">
    <field name="act_from" ref="act_draft"/>
    <field name="act_to" ref="act_open"/>
    <field name="condition">True</field>
    <field name="signal">open</field>
</record>
```

En les *transitions* especifiquem de quina *activity* es surt i a quina s'arriba.

Podem posar una condició, la qual cosa farà que només puguem saltar d'estat si es compleix (la podem definir directament al XML o cridar un mètode del model).

També podem definir un `signal`. Si no en posem, la condició s'avaluarà automàticament després de canviar d'*activity* i en cada modificació del registre. En canvi, si hi ha `signal` només es farà quan es rebi aquest senyal, ja sigui per codi o amb un botó a la vista.

## Detalls interessants

Per exemple, podem fer un camp `required` o `readonly` depenent de l'estat.

```
"paid": fields.boolean(
    "Paid",
    readonly=True,
    states={
        "draft": [("readonly", False)],
        "open": [("readonly", False)],
        "unpaid": [("readonly", False)],
    },
),
```

```
"amount_total": fields.integer(
    "Amount total",
    readonly=True,
    states={
        "draft": [("readonly", False)],
        "open": [("readonly", False)],
    }
),
```

## Graf d'estats de l'exemple



## Més informació

https://openerp-server.readthedocs.io/en/latest/workflows.html

https://www.odoo.com/files/memento/OpenERP_Technical_Memento_v0.7.4.pdf
