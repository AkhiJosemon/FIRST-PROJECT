# Generated by Django 4.2.4 on 2023-11-13 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('stocks', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('rprice', models.IntegerField(null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Varient',
                'verbose_name_plural': 'Varients',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='category.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='category.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.variant'),
        ),
    ]
