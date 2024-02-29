from books.models import Book
from books.serializers import BookSerializer, UserSerializer
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication




class BookList(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]



class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdate(generics.UpdateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class BookDelete(generics.DestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



######### User
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer