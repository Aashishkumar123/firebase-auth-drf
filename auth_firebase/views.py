from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from auth_firebase.authentication import FirebaseAuthentication
from auth_firebase.serializers import StudentSerializer
from auth_firebase.models import Student


class StudentAPIView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]

    def get(self, request):
        students = Student.objects.all()
        student_serializer = StudentSerializer(students, many = True)
        response = {
            'status' : status.HTTP_200_OK,
            'data' : student_serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
