import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from .models import ItemModel
from datetime import date
from attributedict.collections import AttributeDict


class MaterializeCssCheckBoxColumn(tables.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": 
bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})

        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = AttributeDict(default, **(specific or general or {}))
        return mark_safe("<input %s/>" % attrs.as_html())


class ItemTable(tables.Table):
    pur_date = tables.Column()
    exp_date = tables.DateColumn(default=date.today())
    check = MaterializeCssCheckBoxColumn()

    class Meta:
        model = ItemModel
        fields = ('check', 'item_name', 'pur_date', 'exp_date', 'cal')
