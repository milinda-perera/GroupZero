from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from django.core.files.storage import default_storage


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

# delete member by id
class DeleteMemberView(generics.DestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

# to create new project
class CreateProjectView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Extract the project_pics files from the request
        project_pics_files = self.request.FILES.getlist('project_pics')

        # Save the files and collect their paths
        file_paths = []
        for file in project_pics_files:
            path = default_storage.save(f'Project_Pictures/{file.name}', file)
            file_paths.append(path)

        # Pass the paths to the serializer for saving
        serializer.save(project_pics=file_paths)
