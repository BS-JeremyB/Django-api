from rest_framework import serializers
from .models import Book


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=150)
#     description = serializers.CharField()
#     publication_date = serializers.DateField()
#     genre = serializers.CharField(max_length=50)
#     note = serializers.FloatField(default=0)

#REFACTORISATION

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','description','publication_date','genre','note']

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