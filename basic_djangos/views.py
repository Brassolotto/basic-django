from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """Página principal de Basic Django."""
    return render(request, 'basic_djangos/index.html')

def topics(request):
    """Página de tópicos de Basic Django."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'basic_djangos/topics.html', context)

def topic(request, topic_id):
    """Página de detalhes de um tópico específico."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'basic_djangos/topic.html', context)

def new_topic(request):
    """Adiciona um novo tópico."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulário em branco.
        form = TopicForm()
    else:
        # Dados de POST submetidos; processa os dados.
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'basic_djangos/new_topic.html', context)
