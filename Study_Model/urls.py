
from django.contrib import admin
from django.urls import path, include
import Blog.views
# import port.views
# import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Blog.views.home, name='home'), 
    path('blog/', include('Blog.urls')),
    path('portfolio/', include('port.urls')),
    path('accounts/', include('accounts.urls')),
]