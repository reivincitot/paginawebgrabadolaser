import uuid
from django.db import models
from django.utils import timezone
from django.contrib.postgrest.fields import ArrayField, JSONfield
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from decimal import Decimal


class TimeStampedModel(models.Model):
    """Modelo base con timestamps para auditoria"""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    created_by = models.UUIField(null=True, blank=True, editable=False)
    updated_by = models.UUIField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """Modelo base con soft delete"""
    is_active = models.BooleanField(default=True, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.UUIField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self, user_id=None):
        self.is_active = False
        self.deleted_at = timezone.now()
        self.deleted_by = user_id
        self.save()

class ProductBase(TimeStampedModel, SoftDeleteModel):
    """Producto base con todas las características empresariales"""
    class ProductType(models.TextChoices):
        BUSINESS_CARD = 'BUSINESS_CARD',_('Tarjeta de Presentación')
        ID_PLATE = 'ID_PLATE',_('Placa de identificación')
        AWARD = 'AWARD',_('Trofeo/Premio'),
        SIGN = 'SIGN',_('Letrero/Señalización')
        CUSTOM = 'CUSTOM',_('Producto Personalizado')

    class MaterialType(models.TextChoices):
        ACRYLIC = 'ACRYLIC',_('Acrylic'),
        WOOD = 'WOOD', _('Madera'),
        METAL = 'METAL', _('Metal'),
        PLASTIC = 'PLASTIC', _('Plástico')
        GLASS = 'GLASS', _('Vidrio')
        LEATHER = 'LEATHER', _('Cuero')
        MULTI = 'MULTI', _('Combinado')

    class ProductColor(models.TextChoices):
        RED = 'RED',_('Rojo')
        BLACK = 'BLACK', _('Negro')
        BLUE = 'BLUE', _('Azul')
        SILVER = 'SILVER', _('Plateado')
        YELLOW = 'YELLOW', _('Amarillo')
        PINK = 'PINK',_('Rosa')


    class ProductImage(models.ImageField):


    id = models.UUIField(primary_key=True, default=uuid.uuid4(), editable=False)
    sku = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text=_('SKU único del producto (ej: LASER-BC-OO1')
    )
    upc = models.CharField(max_length=50, blank=True, db_index=True, help_text=_('Código de barras'))

    # Vendedor/Tenant (multitenancy)
    vendor_id = models.UUIField(db_index=True, help_text=_('ID del vendedor/artista'))
    tenant_id = models.UUIField(db_index=True, help_text=_('ID de la organización'))

    #Información básica
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True)
    short_description = models.CharField(max_length=200)
    keywords = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        help_text=_('Palabras clave para búsqueda')
    )

    #Categorización
    product_type = models.CharField(
        max_length=50,
        choices=ProductType.choices,
        db_index=True,
    )
    category_id = models.UUIField(db_index=True, null=True, blank=True)
    tags= ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        help_text=_('Etiquetas para filtrado')
    )

    # Precios y comisiones
    base_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
    )
    compare_at_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_('Precio de comparación (antes del descuento')
    )
    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_('Costo de producción')
    )
    commission_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('15.00'), # 15% de comisión por defecto, a revisar
        help_text=_('Porcentaje de comisión para el market place')
    )
    tax_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('19.00'),
        help_text=_('Porcentaje de impuesto')
    )

    #Inventario avanzado
    stock_quantity = models.IntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=10)
    backorder_allowed = models.BooleanField(default=False)
    max_order_quantity = models.PositiveIntegerField() # esto debería ser igual a la maxima capacidad almacenada de dicho producto
    min_order_quantity = models.PositiveIntegerField(default=1)

    # Dimensiones y Peso
    weight_grams = models.FloatField(help_text=_('Cantidad en gramos'))
    length_mm = models.FloatField(help_text=_('Largo en mm'))
    width_mm = models.FloatField(help_text=_('Ancho en mm'))
    depth_mm = models.FloatField(help_text=_('Espesor en mm'))

    # Materiales y acabados
    primary_material = models.CharField(
        max_length=50,
        choices=MaterialType.choices,
        db_index=True
    )
    available_materials = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True
    )
    available_finishes = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True,
        help_text=_('Acabados disponibles: mate, brillo, texturizado, etc')
    )
    available_colors = ArrayField(
        models.CharField(max_length=50),
        default=list,
        help_text=_('Colores disponibles: Azul, Rojo, Plateado, Negro, ...')
    )

    # Tiempos de producción
    production_days = models.PositiveIntegerField(
        default=3,
        help_text=_('Días hábiles para producción')
    )
    shipping_days = models.PositiveIntegerField(
        default=2,
        help_text=_('Días hábiles para envío')
    )
    rush_available = models.BooleanField(default=False)
    rush_surcharge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    # Métricas y rendimiento
    view_count = models.PositiveIntegerField(default=0)
    purchase_count = models.PositiveIntegerField(default=0)
    wishlist_count = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    review_count = models.PositiveIntegerField(default=0)

    # SE0 y marketing
    meta_title = models.charField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = ArrayField(
        models.CharField(max_length=50),
        default=list,
        blank=True
    )

