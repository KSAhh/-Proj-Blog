from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
import port

urlpatterns = [
    path('portfolio/', port.views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)