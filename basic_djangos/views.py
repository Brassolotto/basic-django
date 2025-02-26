from django.shortcuts import render
from .models import Topic

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
