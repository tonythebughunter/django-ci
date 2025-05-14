from rest_framework import serializers
from home.models import Student
from posts.models import Post

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = "__all__"
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Post
        fields = "__all__"

