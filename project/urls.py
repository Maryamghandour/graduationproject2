from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("question.urls")),
    path("programs/", include("program.urls")),
    path("stories/", include("story.urls")),
    path("researches/", include("research.urls")),
    path("profiles/", include("profiles.urls")),
    path("donate/", include("donate.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
