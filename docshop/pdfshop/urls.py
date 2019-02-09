# from django.contrib import admin
# from django.urls import include, path
#
# # urlpatterns = [
# #     path('pdfshop/', include('pdfshop.urls')),
# #     path('admin/', admin.site.urls),
# # ]
#
# from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views
#
# from pdfshop import views as core_views
#
#
# urlpatterns = [
#     path(r'^$', core_views.home, name='home'),
#     path(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
#     path(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
#     path(r'^signup/$', core_views.signup, name='signup'),
# ]

# NOTKA: Polaczenie z baza danych MySQL
# W celu instalacji mysqlclient potrzeba komend:
#
# > sudo apt-get update
# > sudo apt-get install python3-dev
# > sudo apt-get install libmysqlclient-dev
# > pip3 install mysqlclient
#
# mozna tez teoretycznie uzyc pymysql