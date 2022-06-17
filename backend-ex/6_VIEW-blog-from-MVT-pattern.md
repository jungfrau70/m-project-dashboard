### Under the MVT Pattern
### 4th, create VIEWs

(방법1) MVT 패턴
#### 1. Model import
#### 2. Template_name 정의 


WORKDIR="/root/coc-lens/backend"
cd $WORKDIR


######################################################################
# 1. Create home view
######################################################################

cat <<EOF | tee mysite/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
EOF


######################################################################
# 2. Create blog view
######################################################################

cat <<EOF | tee blog/views.py
from django.views.generic import ListView,DetailView
from blog.models import Post

class PostLV(ListView):
    model = Post
    # template_name = 'blog/post_list.html'     # 디폴드 값으로 생략 가능

class PostDV(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'   # 디폴트 설정 값으로 생략 가능
EOF

