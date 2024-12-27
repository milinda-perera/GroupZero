from django.urls import path
from .views import *

urlpatterns = [
    path("create/member/", CreateMemberView.as_view(), name="memeber_create"),
    path("search/member/<int:id>", MemberDetailView.as_view(), name="member_details"),
    path("view/members/", AllMemberView.as_view(), name="all_members")
]
