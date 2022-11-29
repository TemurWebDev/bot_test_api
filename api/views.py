from rest_framework.generics import CreateAPIView,ListAPIView
from .serializer import Postserializer
from .models import Post

class PostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer


class PostlistView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
