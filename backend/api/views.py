from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *


# to create new user
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# to create new member
class CreateMemberView(generics.CreateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

# get member buy id
class MemberDetailView(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

# get all members details
class AllMemberView(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny] 
