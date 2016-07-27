from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'DJ3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'accounts/login/$','DJ3.views.login'),
    url(r'accounts/auth/$','DJ3.views.auth_view'),
    url(r'accounts/logout/$','DJ3.views.logout'),
   # url(r'accounts/loggedin/$','DJ3.views.loggedin'),
    url(r'accounts/invalid/$','DJ3.views.invalid_login'),
    url(r'accounts/register/$','DJ3.views.register_user'),
    url(r'accounts/register_success/$','DJ3.views.register_success'),
]
