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
    revenue_cagr = cagr_data.Revenue_CAGR * 100 if cagr_data.Revenue_CAGR is not None else None
    op_inc_cagr = cagr_data.Op_Inc_CAGR * 100 if cagr_data.Op_Inc_CAGR is not None else None
    net_inc_exc_ext_cagr = cagr_data.Net_Inc_exc_ext_CAGR * 100 if cagr_data.Net_Inc_exc_ext_CAGR is not None else None
    eps_cagr = cagr_data.EPS_CAGR * 100 if cagr_data.EPS_CAGR is not None else None
    dividend_cagr = cagr_data.Dividend_CAGR * 100 if cagr_data.Dividend_CAGR is not None else None
    cashops_cagr = cagr_data.CashOps_CAGR * 100 if cagr_data.CashOps_CAGR is not None else None
    capex_cagr = cagr_data.Capex_CAGR * 100 if cagr_data.Capex_CAGR is not None else None
    equity_cagr = cagr_data.Equity_CAGR * 100 if cagr_data.Equity_CAGR is not None else None



    # Round the values to 2 decimal places
    revenue_cagr = Decimal(revenue_cagr).quantize(Decimal('0.00')) if revenue_cagr is not None else None
    op_inc_cagr = Decimal(op_inc_cagr).quantize(Decimal('0.00')) if op_inc_cagr is not None else None
    net_inc_exc_ext_cagr = Decimal(net_inc_exc_ext_cagr).quantize(Decimal('0.00')) if net_inc_exc_ext_cagr is not None else None
    eps_cagr = Decimal(eps_cagr).quantize(Decimal('0.00')) if eps_cagr is not None else None
    dividend_cagr = Decimal(dividend_cagr).quantize(Decimal('0.00')) if dividend_cagr is not None else None
    cashops_cagr = Decimal(cashops_cagr).quantize(Decimal('0.00')) if cashops_cagr is not None else None
    capex_cagr = Decimal(capex_cagr).quantize(Decimal('0.00')) if capex_cagr is not None else None
    equity_cagr = Decimal(equity_cagr).quantize(Decimal('0.00')) if equity_cagr is not None else None
    

    
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
    # Fetch CAGR data for this stock
    cagr_data = CAGR.objects.get(StockID=stock.pk)

    # Fetch stock sector and sector name
    stock_sector = StockSector.objects.get(StockID=stock.pk)
    sector = Sector.objects.get(ID=stock_sector.SectorID)
    sector_name = sector.SectorName.title()

    # Fetch country and country name
    country = Country.objects.get(ID=stock.CountryID)
    country_name = country.LongName

    # Calculate Dividend CAGR as percentage
    dividend_cagr = cagr_data.Dividend_CAGR * 100 if cagr_data.Dividend_CAGR is not None else None

    # Round the Dividend CAGR to 2 decimal places
    dividend_cagr = Decimal(dividend_cagr).quantize(Decimal('0.00')) if dividend_cagr is not None else None

    # Calculate financial data
    fin_data_latest = {
        'P_E': cagr_data.P_E if cagr_data.P_E else 0.00,
        'Yield_Percent': cagr_data.Yield_Percent * 100 if cagr_data.Yield_Percent else 0.00,
        'Price_HiLo': cagr_data.Price_HiLo * 100 if cagr_data.Price_HiLo else 0.00,
    }

    return {
        'stock': stock,
        'sector_name': sector_name,
        'country_name': country_name,
        'fin_data_latest': fin_data_latest,
        'cagr_data': cagr_data,
        'dividend_cagr': dividend_cagr,  # Dividend CAGR as percentage
    }


def stock_screener(request):
    # get filter parameters from request
    country_id = request.GET.get('country')
    pe_from = request.GET.get('pe_from')
    pe_to = request.GET.get('pe_to')
    dividend_from = request.GET.get('dividend_from')
    dividend_to = request.GET.get('dividend_to')

    # initialize query set
    stocks_list = Stock.objects.all()

    # filter stocks based on filter parameters
    if country_id:
        stocks_list = stocks_list.filter(CountryID=country_id)

    if pe_from and pe_to:
        pe_from = float(pe_from)
        pe_to = float(pe_to)
        stocks_list = stocks_list.filter(cagr__P_E__gte=pe_from, cagr__P_E__lte=pe_to)

    if dividend_from and dividend_to:
        dividend_from = float(dividend_from)
        dividend_to = float(dividend_to)
        stocks_list = stocks_list.filter(cagr__Yield_Percent__gte=dividend_from/100, cagr__Yield_Percent__lte=dividend_to/100)

    # pagination
    paginator = Paginator(stocks_list, 20)  # Show 20 stocks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # get other necessary data
    countries = Country.objects.all()
    stocks_data = []
    for stock in page_obj:
        stock_data = get_stock_data(stock)
        stocks_data.append(stock_data)

    return render(request, 'stock_screener.html', {'stocks_data': stocks_data, 'page_obj': page_obj, 'countries': countries})

def dividend_screener(request):
    # get filter parameters from request
    country_id = request.GET.get('country')
    dividend_from = request.GET.get('dividend_from')
    dividend_to = request.GET.get('dividend_to')
    dividend_cagr_from = request.GET.get('dividend_cagr_from')
    dividend_cagr_to = request.GET.get('dividend_cagr_to')

    # initialize query set
    stocks_list = Stock.objects.all()

    # filter stocks based on filter parameters
    if country_id:
        stocks_list = stocks_list.filter(CountryID=country_id)

    if dividend_from and dividend_to:
        dividend_from = float(dividend_from)
        dividend_to = float(dividend_to)
        stocks_list = stocks_list.filter(cagr__Yield_Percent__gte=dividend_from, cagr__Yield_Percent__lte=dividend_to)

    # New: filter stocks based on Dividend CAGR
    if dividend_cagr_from and dividend_cagr_to:
        dividend_cagr_from = float(dividend_cagr_from) / 100  # Converting to decimal
        dividend_cagr_to = float(dividend_cagr_to) / 100  # Converting to decimal
        stocks_list = stocks_list.filter(cagr__Dividend_CAGR__gte=dividend_cagr_from, cagr__Dividend_CAGR__lte=dividend_cagr_to)

    # pagination
    paginator = Paginator(stocks_list, 20)  # Show 20 stocks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # get other necessary data
    countries = Country.objects.all()
    stocks_data = []
    for stock in page_obj:
        stock_data = get_stock_data(stock)
        stocks_data.append(stock_data)

    return render(request, 'dividend-screener.html', {'stocks_data': stocks_data, 'page_obj': page_obj, 'countries': countries})












