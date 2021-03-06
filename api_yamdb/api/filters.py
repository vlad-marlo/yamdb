from django_filters import FilterSet, rest_framework
from reviews import models


class TitleFilter(FilterSet):
    """
    Filter for Title model
    """
    genre = rest_framework.CharFilter(
        field_name='genre__slug'
    )
    name = rest_framework.CharFilter(
        lookup_expr='contains', field_name='name'
    )
    category = rest_framework.CharFilter(
        field_name='category__slug'
    )

    class Meta:
        model = models.Title
        fields = (
            'genre__slug',
            'name',
            'category__slug',
            'year',
        )
