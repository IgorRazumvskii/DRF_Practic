import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import Beauty, Coords, Level, Images, CustomUser


class Base64Field(serializers.Field):
    def to_representation(self, obj):
        return str(obj)

    def to_internal_value(self, data):
        try:
            # Convert base64 string to bytes
            return ContentFile(base64.b64decode(data.encode('utf-8')))
        except Exception as e:
            raise serializers.ValidationError('Invalid base64 encoding')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    data = Base64Field()

    class Meta:
        model = Images
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class BeautySerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    level = LevelSerializer()
    #user = UserSerializer()
    images = ImagesSerializer(write_only=True, many=True)

    class Meta:
        model = Beauty
        # fields = '__all__'
        exclude = ('user', )

    def create(self, validated_data):
        print(validated_data)
        coords = validated_data.pop('coords')  # берем координаты
        create_coords = Coords.objects.create(**coords)  # создаем координаты
        level = validated_data.pop('level')  # берем уровень
        create_level = Level.objects.create(**level)  # создаем координаты
        #user = validated_data.pop('user')
        #create_user = CustomUser.objects.get_or_create(**user)
        images = validated_data.pop('images')
        images_list = []
        for image in images:
            image = Images.objects.create(**image)
            images_list.append(image)

        print(image)
        beauty_title = validated_data.pop('beauty_title')
        title = validated_data.pop('title')
        other_titles = validated_data.pop('other_titles')
        connect = validated_data.pop('connect')
        customuser = CustomUser.objects.first()
        create_beauty = Beauty.objects.create(beauty_title=beauty_title,
                                              title=title,
                                              other_titles=other_titles,
                                              connect=connect,
                                              level=create_level,
                                              coords=create_coords,
                                              user=customuser,
                                              )  # создаем экземпляр модели
        create_beauty.images.add(*images_list)
        create_beauty.save()
        return create_beauty

    def update(self, instance, validated_data):
        instance.coords = validated_data.get('coords', instance.coords)
        instance.level = validated_data.get('level', instance.level)
        instance.image = validated_data.get('images', instance.level)
        return instance
