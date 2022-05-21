from django.views.generic import ListView,DetailView
from blog.models import Post

class PostLV(ListView):
    model = Post
    # template_name = 'blog/post_list.html'     # 디폴드 값으로 생략 가능

class PostDV(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'   # 디폴트 설정 값으로 생략 가능