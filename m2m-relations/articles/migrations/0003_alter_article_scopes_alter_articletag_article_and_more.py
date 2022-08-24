# Generated by Django 4.0.4 on 2022-04-25 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_articletag_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='articles', through='articles.ArticleTag', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='articles.tag', verbose_name='Раздел'),
        ),
    ]