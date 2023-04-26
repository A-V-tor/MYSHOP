from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import FeedbackForm
from .models import ImageFeedback, Info
from django.views.generic import CreateView


class FeedbackView(CreateView):
    form_class = FeedbackForm
    extra_context = {'title': 'Обратная связь'}
    template_name = 'communication/feedback.html'

    def form_valid(self, form):
        img_list = self.request.FILES.getlist('images')

        feedback = form.save(commit=False)
        feedback.user = self.request.user
        feedback.save()
        [
            ImageFeedback.objects.create(image=i, feedback=feedback)
            for i in img_list
        ]

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Сообщение отправлено',
        )

        return redirect('feedback')


def info_view(request):
    data = Info.objects.first()
    title = 'Информационная страничка'
    description = 'Нет никаких записей в данный момент.'

    if data:
        title = data.title
        description = data.description
    return render(
        request,
        'communication/info.html',
        context={'title': title, 'description': description},
    )
