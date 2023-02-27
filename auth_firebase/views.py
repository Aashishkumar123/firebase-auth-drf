from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from auth_firebase.authentication import FirebaseAuthentication


class TestAPIView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [FirebaseAuthentication]

    def get(self, request):
        response = {
            'status' : status.HTTP_200_OK
        }
        return Response(response, status=status.HTTP_200_OK)
