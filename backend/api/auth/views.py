
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status, generics

from users.serializer import UserSerializer


class LoginView(TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """

    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            userdata = None
            userdata = UserSerializer(serializer.user).data
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = Response(
            {
                "tokens": {**serializer.validated_data},
                "user": {**userdata}
            },
            status=status.HTTP_200_OK,
        )
        return response
