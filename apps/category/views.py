from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework import viewsets
# rest framework
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination

from category.models import categoryModel
from subject.models import subjectModel
from category.serializers import CategorySerializer

# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class categoryView(View):
    def get(self, request, id):
        category = get_object_or_404(categoryModel, id=id)
        subjects = subjectModel.objects.filter(category=category).order_by('-pub_date', '-update_time')
        page = request.GET.get('p', 1)

        p = Paginator(subjects, per_page=18)  # , per_page=page - 1
        subjects = p.page(page)

        breadcrumbs = []
        breadcrumbs.append({'title': category.name})
        breadcrumbs.append({'title': '第%d页' % subjects.number})

        return render(request, 'category/category.html',
                      context={'subjects': subjects, 'category': category, 'breadcrumbs': breadcrumbs})


# class CategoryListView(APIView):
#     """
#     列出所有的分类或者创建一个新的分类。
#     """
#
#     def get(self, request, format=None):
#         categorys = categoryModel.objects.all()
#         serializer = CategorySerializer(categorys, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    列出所有的主题或者创建一个新的主题。
    """
    queryset = categoryModel.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


    filter_backends = ( DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('inHead',)
    search_fields = ('name',)
    ordering_fields = ('order',)