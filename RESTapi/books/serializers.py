from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=150)
#     description = serializers.CharField()
#     publication_date = serializers.DateField()
#     genre = serializers.CharField(max_length=50)
#     note = serializers.FloatField(default=0)

#REFACTORISATION

class BookSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['id','title','description','publication_date','genre','note', 'owner']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.note = validated_data.get('note', instance.note)
        instance.save()

        return instance
    


class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']