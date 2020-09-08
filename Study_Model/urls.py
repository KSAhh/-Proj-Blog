
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# import Blog.views
# import port.views
# import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Blog.views.home, name='home'), 
    path('blog/', include('Blog.urls')),
    path('portfolio/', include('port.urls')),
    # path('accounts/', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)