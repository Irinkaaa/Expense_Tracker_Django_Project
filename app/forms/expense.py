from django import forms
from app.forms.common import DisabledFormMixin
from app.models import Expenses


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'


class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
