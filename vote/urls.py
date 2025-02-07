from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.vote_home, name='vote_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.VoteDetailView.as_view(), name='vote-detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
