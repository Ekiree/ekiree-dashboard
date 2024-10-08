from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.EDIndex, name='EDIndex'),
    path('sharedlist/', views.SharedList, name='SharedList'),
    path('sharedlist/<str:shared_url>', views.SharedList, name='SharedList'),
    path('courselist/', views.CourseList, name='CourseList'),
    path('courselist/<str:username>', views.CourseList, name='CourseList'),
    path('majmin/', views.MajorMinor, name='MajorMinor'),
    path('educationaldesign/', views.ED, name="ED"),
    path('educationaldesign/<str:username>', views.ED, name="ED"),
    path('api/subject/', views.API, name='API'),
    path('api/subject/<str:subj>/', views.API, name='API'),
    path('api/subject/<str:subj>/<str:num>/', views.API, name='API'),
    path('addcourse/', views.AddCourse, name='AddCourse'),
    path('deletecourse/', views.DeleteEDCourse, name='deleteEDCourse'),
    path('editcourse/', views.EditEDCourse, name='editEDCourse'),
    path(
        'editcourse/<int:edcourse_id>',
        views.EditEDCourse,
        name='editEDCourse'
    ),
    path('goals/', views.Goals, name='AllGoals'),
    path('addgoal/', views.AddEducationalGoal, name="AddGoal"),
    path('editgoal/', views.EditEDGoal, name="EditGoal"),
    path('editgoal/<int:goal_id>', views.EditEDGoal, name="EditGoal"),
    path('deletemajor/', views.DeleteMajor, name='deleteMajor'),
    path('deleteminor/', views.DeleteMinor, name='deleteMinor'),
    path(
        'deleteedgoal/',
        views.DeleteEducationalGoal,
        name='deleteEducationalGoal'
    ),
    path('approveED/', views.ApproveED, name='ApproveED'),
    path(
        'approvedcourselist/',
        views.ApprovedCourseList,
        name='ApprovedCourses'
    ),
    path(
        'approvedcourselist/<str:username>',
        views.ApprovedCourseList,
        name='ApprovedCourses'
    ),
    path('replaceappcourse/', views.ReplaceAppCourse, name='replaceAppCourse'),
    path(
        'replaceappcourse/<int:appcourse_id>',
        views.ReplaceAppCourse,
        name='replaceAppCourse'
    ),
    path(
        'ApproveAppCourseReplacement/',
        views.ApproveAppCourseReplacement,
        name='approveReplace'
    ),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
