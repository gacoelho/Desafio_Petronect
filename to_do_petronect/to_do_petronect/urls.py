from django.contrib import admin
from django.urls import path
from to_do.views import index, creat_task_view, edit_task_view, delete_task_view, check_task
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('task_form/', creat_task_view),
    path('edit_task/<int:task_id>/', edit_task_view),
    path('del_task/<int:task_id>/', delete_task_view),
    path('check_task/<int:task_id>/', check_task),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
