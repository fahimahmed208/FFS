
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #dee
    path('admin/', admin.site.urls),
    path('mm/',views.makemoney),
    path('contact/',views.contact),
    #path('send/',views.sendInfo),
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    #apps
    path('mm/ac/', include('accounts.urls')),
    path('acc/', include('accs.urls')),
    path('mm/acc/', include('accs.urls')),
    path('mm/st/', include('stores.urls')),
    path('pl/', include('plans.urls')),
    path('dl/', include('dguys.urls')),
    path('en/', include('enrolments.urls')),
    path('pay/', include('payments.urls')),
    #alim
    path('send/',views.sendemail)

]
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

