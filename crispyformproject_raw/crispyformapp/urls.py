from django.urls import path
from django.contrib import admin
from crispyformapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/',views.student_data,name='data'),
    path('',views.fetching_data,name='home'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('student_page/',views.student_page,name='student_page'),
    path('no_entry/',views.no_entry,name='no_entry'),

    path('courses/',views.courses_view,name='courses'),
    path('collages/',views.collages_view,name='collages'),
    path('locations/',views.locations_view,name='locations'),
    path('branches/',views.branches_view,name='branches'),
    path('institutions/',views.institutions_view,name='institutions'),

    path('add_course/',views.add_course, name='add_course'),
    path('add_collage/',views.add_collage, name='add_collage'),
    path('add_location/',views.add_location, name='add_location'),
    path('add_branch/',views.add_branch, name='add_branch'),
    path('add_institute/',views.add_institute, name='add_institute'),

    path('update_course/<pk>',views.update_course, name='update_course'),
    path('update_collage/<pk>',views.update_collage, name='update_collage'),
    path('update_location/<pk>',views.update_location, name='update_location'),
    path('update_branch/<pk>',views.update_branch, name='update_branch'),
    path('update_institute/<pk>',views.update_institute, name='update_institute'),

    path('delete_course/<pk>',views.delete_course, name='delete_course'),
    path('delete_collage/<pk>',views.delete_collage, name='delete_collage'),
    path('delete_location/<pk>',views.delete_location, name='delete_location'),
    path('delete_branch/<pk>',views.delete_branch, name='delete_branch'),
    path('delete_institute/<pk>',views.delete_institute, name='delete_institute'),

    path('add_marks/',views.add_marks,name='add_marks'),
    path('fetch_marks/',views.fetch_marks,name='fetch_marks'),

    path('modify_data/',views.modify_data,name='modify_data'),
]



