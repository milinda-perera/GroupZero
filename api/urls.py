from django.urls import path
from .views import *

urlpatterns = [
    path("create/member/", CreateMemberView.as_view(), name="memeber_create"),
    path("search/member/<int:id>", MemberDetailView.as_view(), name="member_details"),
    path("view/members/", AllMemberView.as_view(), name="all_members"),
    path("delete/member/<int:id>", DeleteMemberView.as_view(), name="delete_member"),
    path("create/project/", CreateProjectView.as_view(), name="project_create"),
    path("update/member/<int:id>", UpdateMemberView.as_view(), name="update_member"),
    path("projects/", AllProjects.as_view(), name="all_projects"),
]
