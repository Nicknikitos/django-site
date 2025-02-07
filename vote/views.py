from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def vote_home(request):
    vote = Articles.objects.all()
    return render(request, 'vote/vote_home.html', {'vote': vote})


class VoteDetailView(DetailView):
    model = Articles
    template_name = 'vote/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vote')
        else:
            error = 'Форма была неверной'



    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'vote/create.html', data)