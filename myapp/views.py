from django.shortcuts import render, get_object_or_404
from .models import Country, Stock, FinData, CoFinExport, CAGR, StockSector, Sector
from django.db.models import Max
from datetime import timedelta
from decimal import Decimal
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})

# Main Stock Page View
def stock_detail(request, slug):
    stock = get_object_or_404(Stock, slug=slug)
    
    # Get the CAGR data for this stock
    cagr_data = CAGR.objects.get(StockID=stock.pk)    

    # Modify the fields as percentages
    revenue_cagr = cagr_data.Revenue_CAGR * 100
    op_inc_cagr = cagr_data.Op_Inc_CAGR * 100
    net_inc_exc_ext_cagr = cagr_data.Net_Inc_exc_ext_CAGR * 100
    eps_cagr = cagr_data.EPS_CAGR * 100
    dividend_cagr = cagr_data.Dividend_CAGR * 100
    cashops_cagr = cagr_data.CashOps_CAGR * 100
    capex_cagr = cagr_data.Capex_CAGR * 100
    equity_cagr = cagr_data.Equity_CAGR * 100

    # Round the values to 2 decimal places
    revenue_cagr = Decimal(revenue_cagr).quantize(Decimal('0.00'))
    op_inc_cagr = Decimal(op_inc_cagr).quantize(Decimal('0.00'))
    net_inc_exc_ext_cagr = Decimal(net_inc_exc_ext_cagr).quantize(Decimal('0.00'))
    eps_cagr = Decimal(eps_cagr).quantize(Decimal('0.00'))
    dividend_cagr = Decimal(dividend_cagr).quantize(Decimal('0.00'))
    cashops_cagr = Decimal(cashops_cagr).quantize(Decimal('0.00'))
    capex_cagr = Decimal(capex_cagr).quantize(Decimal('0.00'))
    equity_cagr = Decimal(equity_cagr).quantize(Decimal('0.00'))
    
    fin_data = get_financials_for_stock(stock.pk)
    years = sorted(next(iter(next(iter(fin_data.values())).values())).keys())  # get the years from one of the data dictionaries   
    
    # Fetch the stock's sector ID
    stock_sector = StockSector.objects.get(StockID=stock.pk)
    sector = Sector.objects.get(ID=stock_sector.SectorID)
    sector_name = sector.SectorName.title()
    
    # Fetch the stock's country ID
    country = Country.objects.get(ID=stock.CountryID)
    country_name = country.LongName  # The name of the country
        
    context = {
        'stock': stock,
        'sector_name': sector_name,
        'country_name': country_name,
        'cagr_data': cagr_data,
        'revenue_cagr': revenue_cagr,
        'op_inc_cagr': op_inc_cagr,
        'net_inc_exc_ext_cagr': net_inc_exc_ext_cagr,
        'eps_cagr': eps_cagr,
        'dividend_cagr': dividend_cagr,
        'cashops_cagr': cashops_cagr,
        'capex_cagr': capex_cagr,
        'equity_cagr': equity_cagr,
        'years': years,
        'fin_data': fin_data,
    }

    return render(request, 'stock_detail.html', context)


def get_financials_for_stock(stock_id):
    fin_data_names = {
        'income statement': ['revenue', 'operating income', 'net income exc extra', 'net income',
                             'diluted EPS exc extra', 'diluted EPS inc extra', 'dividend ps', 'shares outstanding'],
        'cashflow statement': ['cash from operations', 'depreciation', 'capital expenditure',
                               'total cash from investing', 'issuance - retirement of stock',
                               'issuance - retirement of debt', 'total cash from financing', 'starting cash',
                               'ending cash'],
        'balance sheet': ['current assets', 'goodwill', 'intangibles', 'total assets', 'current liabilities',
                          'long term debt', 'total liabilities', 'shareholder equity']
    }
    fin_data = {statement.title(): {name.title(): {} for name in names} for statement, names in fin_data_names.items()}

    for statement, names in fin_data_names.items():
        for name in names:
            fin_id = FinData.objects.filter(FinDataName=name).values('ID')[0]['ID']
            data_points = CoFinExport.objects.filter(StockID=stock_id, FinDataID=fin_id).order_by('PeriodEnd')
            for data_point in data_points:
                year = data_point.PeriodEnd.year
                value = data_point.RepValue
                # Round 'Shares Outstanding' to the nearest whole number
                if name == 'shares outstanding':
                    value = round(value)
                # Add commas to numbers over 1,000
                if isinstance(value, (int, float)) and value >= 1000:
                    value = '{:,.0f}'.format(value)
                fin_data[statement.title()][name.title()][year] = value

    return fin_data


def get_stock_data(stock):
    cagr_data = CAGR.objects.get(StockID=stock.pk)

    # get latest date financial data
    latest_date = CoFinExport.objects.filter(StockID=stock.pk).aggregate(Max('PeriodEnd'))['PeriodEnd__max']

    # list of financial data names we need to fetch
    fin_data_names = ['PE ratio', 'dividend', 'eps']

    fin_data_latest = {}
    if latest_date is not None:
        for name in fin_data_names:
            try:
                fin_id = FinData.objects.get(FinDataName=name).ID
                data_point = CoFinExport.objects.get(StockID=stock.pk, FinDataID=fin_id, PeriodEnd=latest_date)
                fin_data_latest[name] = data_point.RepValue
            except FinData.DoesNotExist or CoFinExport.DoesNotExist:
                fin_data_latest[name] = None

    stock_sector = StockSector.objects.get(StockID=stock.pk)
    sector = Sector.objects.get(ID=stock_sector.SectorID)
    sector_name = sector.SectorName.title()

    country = Country.objects.get(ID=stock.CountryID)
    country_name = country.LongName

    return {
        'stock': stock,
        'sector_name': sector_name,
        'country_name': country_name,
        'fin_data_latest': fin_data_latest,  
        'cagr_data': cagr_data,
    }

def stock_screener(request):
    stocks_list = Stock.objects.all()
    paginator = Paginator(stocks_list, 20)  # Show 50 stocks per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    stocks_data = []

    for stock in page_obj:
        stock_data = get_stock_data(stock)
        stocks_data.append(stock_data)

    return render(request, 'stock_screener.html', {'stocks_data': stocks_data, 'page_obj': page_obj})








