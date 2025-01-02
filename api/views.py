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

# update member view
class UpdateMemberView(generics.UpdateAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

# get member buy id
class MemberDetailView(generics.RetrieveAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

# get all members details
class AllMemberView(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated] 

# delete member by id
class DeleteMemberView(generics.DestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

# to create new project
class CreateProjectView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

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

# get all projects
class AllProjects(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

# get project by id
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# update project by id  
class UpdateProjectView(generics.UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# delete project by id  
class DeleteProjectView(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


# to create new review
class CreateReviewView(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


# check if the current user is a member
class IsMemberView(generics.ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Members.objects.filter(username=self.request.user)

