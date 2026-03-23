from django.contrib import messages
from django.views.generic import (
    CreateView
)

from .forms import (
    QRCodeForm,
)
from .models import QRCode
from .utils import GeneratorMixin


class QRCodeCreateView(CreateView,GeneratorMixin):
    model = QRCode
    template_name = 'generator/generator.html'
    form_class = QRCodeForm
    context_object_name = 'qr'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        messages.success(request=self.request, message='successful generated')
        return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        # Django already handles rendering the form with errors
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context=context, title='QRcode Generator')


