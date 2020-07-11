
import datetime

import factory
from formaster.models import Form


class FormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Form

    user_id = factory.Sequence(lambda n: n + 1)
    form_title = factory.Sequence(lambda n: f"form_title_{n}")
    created_at = factory.LazyFunction(datetime.datetime.now)


#     user_id = models.IntegerField()
#     form_title = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now=True)


# class PostFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Post

#     user_id = factory.Sequence(lambda n: n + 1)
#     pub_date_time = factory.LazyFunction(datetime.datetime.now)
#     post_content = factory.Sequence(lambda n: "post_content_{0}".format(n + 1))


# class CommentFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Comment

#     post = factory.SubFactory(PostFactory)
#     comment_text = factory.Sequence(
#         lambda n: "comment_content_{0}".format(n + 1))
#     pub_date_time = factory.LazyFunction(datetime.datetime.now)
#     parent_comment = factory.Sequence(lambda n: n + 1)
#     user_id = factory.Sequence(lambda n: n + 1)


# class ReactionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Reaction
#     comment = factory.SubFactory(CommentFactory)
#     post = factory.SubFactory(PostFactory)
#     user_id = factory.Sequence(lambda n: n + 1)
#     reaction_type = factory.Iterator(reaction_types)


# class ReplyFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Comment

#     user_id = factory.Sequence(lambda n: n)
#     comment_text = factory.Sequence(lambda n: "NiceComment %03d" % n)
#     parent_comment = factory.SubFactory(CommentFactory)
