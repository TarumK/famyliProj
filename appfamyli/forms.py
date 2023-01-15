from django import forms
from .models import Town, Team

class MyForm(forms.Form):
    f_town = forms.ModelChoiceField(queryset=Town.objects.all(), label='Города')
    f_team = forms.ModelChoiceField(queryset=Team.objects.none(), label='Бригады')
    # parents = forms.ModelChoiceField(queryset=Parent.objects.all(), label='Фамилии')
    # children = forms.ModelChoiceField(queryset=Child.objects.none(), label='Члены семьи')

    # def __init__(self, *args, **kwargs):
    #     super(MyForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['children'].queryset = Child.objects.none()
    #
    # def clean(self):
    #     cleaned_data = super(MyForm, self).clean()
    #     parent = cleaned_data.get("parents")
    #     children = cleaned_data.get("children")
    #
    #     if parent and not children:
    #         self.fields['children'].queryset = Child.objects.filter(parent=parent)




# from django import forms
# from .models import Parent, Child
#
#
# class MyForm(forms.Form):
#     parent = forms.ModelChoiceField(queryset=Parent.objects.all())
#     child = forms.ModelChoiceField(queryset=Child.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['child'].queryset = Child.objects.none()
#
#         if 'parent' in self.data:
#             try:
#                 parent_id = int(self.data.get('parent'))
#                 self.fields['child'].queryset = Child.objects.filter(parent_id=parent_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty child queryset
#         elif self.instance.pk:
#             self.fields['child'].queryset = self.instance.parent.child_set.order_by('name')
#
#
