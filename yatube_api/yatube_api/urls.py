from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = 'Yatube API.'
API_DESCR = 'A Web API to create and edit blog posts and comments.'

schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/schema/', schema_view),
    path(
        'api/v1/docs/',
        include_docs_urls(title=API_TITLE, description=API_DESCR)
    ),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
