from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)
    
    @classmethod
    def last_record(cls):
        return Product.objects.last()
    
    @classmethod
    def by_rating(cls, rating_value):
        return Product.objects.filter(rating=rating_value)
    
    @classmethod
    def by_rating_range(cls, rating_start, rating_end):
        return Product.objects.filter(rating__range=(rating_start, rating_end))
    
    @classmethod
    def by_rating_and_color(cls, rating_value, color_value):
        return Product.objects.filter(Q(rating=rating_value) & Q(color=color_value))
    
    @classmethod
    def by_rating_or_color(cls, rating_value, color_value):
        return Product.objects.filter(Q(rating=rating_value) | Q(color=color_value))
    
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color__isnull=True).count()
    
    @classmethod
    def below_price_or_above_rating(cls, price_value, rating_value):
        return Product.objects.filter(Q(price_cents__lt=price_value) | Q(rating__gt=rating_value))
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')
    
    @classmethod
    def products_by_manufacturer_with_name_like(cls, manufacturer_name):
        return Product.objects.filter(manufacturer__contains=manufacturer_name)
    
    @classmethod
    def manufacturer_names_for_query(cls, manufacturer_name):
        return Product.objects.filter(manufacturer__contains=manufacturer_name).values_list('manufacturer', flat=True)

    @classmethod
    def not_in_a_category(cls, category_name):
        return Product.objects.exclude(category=category_name)

    @classmethod
    def limited_not_in_a_category(cls, category_name, limit):
        return Product.objects.exclude(category=category_name)[0:limit]

    @classmethod
    def category_manufacturers(cls, category_name):
        return Product.objects.filter(category=category_name).values_list('manufacturer', flat=True)

    @classmethod
    def average_category_rating(cls, category_name):
        return Product.objects.filter(category=category_name).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.order_by((Length('model')).desc()).first().id

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model'))
