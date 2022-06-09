from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_programs),
    path("<int:program>/", views.program_details),
    path("<int:program>/<int:lecture>/", views.program_details),
    path("add", views.add_program),
    path("delete/<int:id>", views.delete_program),
    path("add-lecture/", views.add_lecture),
    path("delete-lecture/<int:id>", views.delete_lecture),
]
