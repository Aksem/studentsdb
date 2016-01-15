from django.core.urlresolvers import reverse
from django.forms import ModelForm, ModelChoiceField, Select
from django.views.generic import UpdateView,DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from .models import Group, Student

class GroupSelector(ModelForm):
    title = ModelChoiceField(
        label='Оберіть групу',
        queryset=Group.objects.all(),
        widget=Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Group
        fields = ('title',)

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'middle_name', 'birthday', 'photo','ticket',
                  'notes', 'student_group')

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm,self).__init__(*args,**kwargs)

        self.helper = FormHelper(self)

        #set form tag attributes
        self.helper.form_action = reverse('students_edit',
        kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        #set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Зберегти', css_class="btn btn-primary"),
            Submit('cancel_button', u'Скасувати',css_class = "btn btn-link"))
