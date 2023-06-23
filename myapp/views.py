from django.shortcuts import render, get_object_or_404
from .models import Country, Stock, CoFinExport
from django.db.models import Max
from datetime import timedelta


# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})


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

        # Calculate the CAGR for each data point
        cagr_data = []
        for data_latest, data_start in zip(fin_data_latest, fin_data_start):
            if data_start and data_latest:
                try:
                    begin_value = data_start.RepValue
                    end_value = data_latest.RepValue
                    cagr = ((end_value / begin_value) ** (1 / 5)) - 1
                    cagr_data.append({
                        'fin_data': data_latest.FinDataID.FinDataName,
                        'cagr': cagr,
                    })
                except ZeroDivisionError:
                    print(f'Error calculating CAGR for {data_latest.FinDataID.FinDataName}: division by zero')
            else:
                print(f'Missing data for {data_latest.FinDataID.FinDataName} on start or end date')
    else:
        fin_data_latest = None
        cagr_data = None
   
    context = {
        'stock': stock,
        'fin_data': fin_data_latest,
        'cagr_data': cagr_data,
    }

    return render(request, 'stock_detail.html', context)



