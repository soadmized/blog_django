from django.views.generic import ListView, DetailView
from . models import Post


class BlogListView(ListView):
   
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'post_detail.html'
   #context_object_name = 'anything_you_want' - имя объекта, который возвращает DetailView для
                                                # использования в шаблоне html (вместо post или object)