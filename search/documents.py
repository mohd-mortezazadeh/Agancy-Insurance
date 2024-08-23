from django.contrib.auth import get_user_model
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from blog.models import Post
from category.models import Category
from tag.models import Tag

User = get_user_model()


@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
        ]


@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()
    category = fields.ObjectField(properties={
        'title': fields.TextField(),
        # 'content': fields.TextField(),
    })
    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'title',
            # 'content',
        ]
        # related_models = [Category]
        # def get_queryset(self):
        #     return super().get_queryset().select_related(
        #     'subcats'
        # )
        # def get_instances_from_related(self, related_instance):
        #     """If related_models is set, define how to retrieve the SubCategory instance(s) from the related model.
        #     The related_models option should be used with caution because it can lead in the index
        #     to the updating of a lot of items.
        #     """
        #     if isinstance(related_instance, Category):
        #         return related_instance.subcategories.all()
        #     return related_instance.category
           


@registry.register_document
class PostDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField(),
        'email': fields.TextField(),
    })
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
        'content': fields.TextField(),
      
   
    })

    content = fields.TextField(fields= {
        "row": {
            "type":"keyword"
        }
    })
    tags = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'title': fields.TextField(),
      
    })
    class Index:
        name = 'posts'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
        related_models = [Category, User]
        
    def get_queryset(self):
        return super().get_queryset().select_related(
        'subcategory'
    )
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, User):
            return related_instance.posts.all()
        elif isinstance(related_instance, Category):
            return related_instance.posts.all()

    class Django:
        model = Post
        fields = [
        
            'title',
            'summary',
            'slug',
            'banner',
            'created',
            'updated',
        ]