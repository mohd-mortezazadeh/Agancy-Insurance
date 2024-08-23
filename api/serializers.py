from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.models import Post
from category.models import Category
from newsletters.models import NewsLetter
from tag.models import Tag

User = get_user_model()
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import email_address_exists

from category.models import Category
from users.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url','pk', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'pk', 'user', 'avatar', 'birthday', 'phone', 'number', 'zip']


class TagSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Tag
            fields = ["url", "pk", "title", 'status', "created", "updated"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Category
            fields = ["url", "pk", "title", "content", "banner", "created", "updated"]


# class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
#         category = CategorySerializer()
#         class Meta:
#             model = SubCategory
#             fields = ["url", "pk", "title", "content", "banner", "category"]


class PostSerializer(serializers.ModelSerializer):
    
    def get_author(self, obj):
        return {
            "id":obj.author.id,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name,
            "email":obj.author.email,
        }
    author = serializers.SerializerMethodField("get_author")
    # subcategory = SubCategorySerializer()
    # tag = TagSerializer(many = True, required = True)
    
    class Meta:
        model = Post
        fields = ["url", "pk", "title", "status", "summary", "banner", "content", "author", "created", "updated", "published_at","category", "tag"]


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
          
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'