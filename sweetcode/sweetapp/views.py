from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
 
class PostAPI(generics.ListCreateAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer