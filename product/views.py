from django.db.models import Q
from django.views import generic
from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger,EmptyPage, InvalidPage, Paginator
# from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.carts import Cart
# from django.shortcuts import render


#Create your views here.
class Home(generic.TemplateView ):
    template_name = 'home.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs, )
        context.update(
            {
                "featured_categories":Category.objects.filter(),
                "featured_products":Product.objects.filter(),
                "sliders":Slider.objects.filter(show=True),
            }
        )
        return context


    


class ProductDetails(generic.DetailView):
    
    model = Product
    slug_url_kwarg = 'slug'

    

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['related_products'] = self.get_object().related
       return context
    template_name = 'product/product-details.html'


class CategorytDetails(generic.DetailView):
    model = Category
    template_name = 'product/category-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['products'] = self.get_object().products.all()
       return context
    
class CustomPaginator:
    def __init__(self, request, queryset, paginted_by) ->None:
        self.paginator = Paginator(queryset, paginted_by)
        self.paginted_by = paginted_by
        self.queryset = queryset
        self.page = request.GET.get('page', 1)

    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)

        return queryset

class ProudctList(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'object_list'
    paginate_by = 5

   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = CustomPaginator(self.request, self.get_queryset(), self.paginate_by)
        quryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['object_list'] = quryset
        context['paginator']=paginator
        return context

class SearchProducts(generic.View):
    def get(self, *args, **kwargs):
        key = self.request.GET.get('key', '')
        products = Product.objects.filter(Q(title__icontains = key)| Q(description__icontains = key))
        context = {
            "products": products,
            "key":key
        }
        return render(self.request, 'product/search-products.html', context)

def order(request):
    firstName = request.GET.get("firstName")
    lastName = request.GET.get("lastName")
    address = request.GET.get("address")
    phone = request.GET.get("phone")
    if firstName:
        Order.objects.create(firstname = firstName, lastname=lastName, address=address, phone=phone).save()
        return redirect("home")
    return render(request, 'order.html')