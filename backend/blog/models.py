from django.db import models

# Create your models here.

class Post(models.Model): # tablename
    # id =, 장고에서 자동으로 만들어 줌 
    title = models.CharField(verbose_name='TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text="smiple description")
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE_DATE', auto_now=True)
    # tags = models.CharField('TAGS') 
    # author = models.CharField('AUTHOR')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.id,)) # 장고에서 자동으로 생성해 줘서, 사용 가능
    
    def get_prev(self):
        return self.get_previouse_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()