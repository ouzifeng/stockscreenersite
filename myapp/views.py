from django.shortcuts import render, get_object_or_404
from .models import Country, Stock, FinData, CoFinExport, CAGR
from django.db.models import Max
from datetime import timedelta
from decimal import Decimal


# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})

# Main Stock Page View
def stock_detail(request, slug):
    stock = get_object_or_404(Stock, slug=slug)

    # Get the most recent date for which data is available for this stock
    latest_date = CoFinExport.objects.filter(StockID=stock.pk).aggregate(Max('PeriodEnd'))['PeriodEnd__max']

    if latest_date is not None:
        # Fetch the financial data for the most recent date
        fin_data_latest = CoFinExport.objects.select_related('FinDataID').filter(StockID=stock.pk, PeriodEnd=latest_date)

        # Get the date 5 years prior to the most recent date
        start_date = latest_date - timedelta(days=5*365)

        # Fetch the financial data for the start date
        fin_data_start = CoFinExport.objects.select_related('FinDataID').filter(StockID=stock.pk, PeriodEnd=start_date)

    else:
        fin_data_latest = None
     
    # Get the CAGR data for this stock
    cagr_data = CAGR.objects.get(StockID=stock.pk)    

    # Modify the Yield_Percent value
    yield_percent = cagr_data.Yield_Percent * 100
    yield_percent = Decimal(yield_percent).quantize(Decimal('0.00'))
   
    context = {
        'stock': stock,
        'fin_data': fin_data_latest,
        'cagr_data': cagr_data,
        'yield_percent': yield_percent,
    }

    return render(request, 'stock_detail.html', context)


