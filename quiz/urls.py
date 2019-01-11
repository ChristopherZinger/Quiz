from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from quizgame.views import QuizIndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quizgame/', include('quizgame.urls', namespace='quizgame')),
    url(r'^$', QuizIndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
