
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index-url'),
    path('add/',views.trade_entry,name='trade-entry'),
    path('report/',views.report_view,name="report-view"),
    path('delete/<int:pk>/',views.delete_record,name="delete-rocord"),
    path('edit/<int:pk>',views.edit_trade,name='edit-trade'),
]

















if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)