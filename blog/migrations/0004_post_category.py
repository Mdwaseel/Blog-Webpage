# Generated by Django 4.2.7 on 2023-11-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Lifestyle', 'Lifestyle'), ('Finance', 'Finance'), ('Education', 'Education'), ('Food_Cooking', 'Food and Cooking'), ('Business_Entrepreneurship', 'Business and Entrepreneurship'), ('Book_Movie_Reviews', 'Book and Movie Reviews'), ('Parenting', 'Parenting'), ('Science_Nature', 'Science and Nature'), ('Art_Creativity', 'Art and Creativity')], default='Lifestyle', max_length=50),
        ),
    ]
