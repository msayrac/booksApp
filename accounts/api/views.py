from rest_framework import generics
from rest_framework.permissions import AllowAny # herkes yorum yapabilir
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from django.contrib.auth.models import User
from reviews.models import Review
from accounts.api.serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Review.objects.all()
    # permission_classes = [AllowAny] # Herkes Okuyabilir. Ancak yorum sadece giriş yapmış kullanıcıya ait
    permission_classes = (AllowAny,) # Herkes acık yorum yapabilir
    serializer_class = RegisterSerializer

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

