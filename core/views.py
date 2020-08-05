from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from .models import CustomUser

class UserCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                #send to login
                #call currentusers
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''''
def currentusers(request):
    cuser = request.user
    duser = CustomUser.objects.exclude(username=cuser.get_username())
    return Response({'loggedin_user':cuser,'userdict':duser})
'''