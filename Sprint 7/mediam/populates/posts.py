import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mediam.settings')

import django
django.setup()

from home.models import Post, Comment
from user.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for item in range(N):
        # Creating fake user
        fake_email = fakegen.email()
        fake_first_name = fakegen.name()
        fake_nick_name = fakegen.name()
        fake_password = fakegen.name()
        fake_phone_number = fakegen.phone_number()
        fake_description = fakegen.text()
        fake_image_user = fakegen.image_url()

        fake_user = User.objects.create(email = fake_email, image = fake_image_user, first_name = fake_first_name, nick_name = fake_nick_name, password = fake_password, phone_number = fake_phone_number, description = fake_description)
        fake_user.save()

        # Creating fake comments
        fake_body = fakegen.text()
        fake_comment = Comment.objects.create(body=fake_body, user=fake_user)
        fake_comment.save()

        # Creating fake post
        fake_image = fakegen.image_url()
        fake_description = fakegen.text()
        fake_likes = fakegen.pyint()

        fake_post = Post.objects.create(image=fake_image, description=fake_description, likes = fake_likes, comments=fake_comment, user=fake_user)
        fake_post.save()


if __name__ == '__main__':
    print('Creando datos...')
    populate(10)
    print('Exito!')