from django import template

register = template.Library()

GF_TO_TV_MAPPING = {
    "ETR": "XETR",
    "LON": "LSE",
    "NYSE": "NYSE",
    "NASDAQ": "NASDAQ",
    "KLSE": "MYX",
    "AMS": "EURONEXT",
    "ASX": "ASX",
    "BCBA": "BCBA",
    "STO": "OMXSTO",
    "HEL": "OMXHEX",
    "BIT": "MIL",
    "BKK": "SET",
    "BME": "BME",
    "BMV": "BMV",
    "BOM": "NSE",
    "BVMF": "BMFBOVESPA",
    "CPH": "OMXCOP",
    "EBR": "EURONEXT",
    "ELI": "EURONEXTLISBON",
    "EPA": "EURONEXT",
    "FRA": "FWB",
    "HKG": "HKEX",
    "IDX": "IDX",
    "IST": "BIST",
    "JSE": "JSE",
    "KRX": "KRX",
    "NZE": "NZX",
    "SGX": "SGX",
    "SWX": "SIX",
    "TPE": "TWSE",
    "TSE": "TSX",
    "TYO": "TSE",
    "VIE": "VIE",
    "WSE": "GPW"
}


@register.filter(name='convert_to_tv_ticker')
def convert_to_tv_ticker(gf_ticker):
    try:
        prefix = gf_ticker.split(":")[0]
        symbol = gf_ticker.split(":")[1]
        tv_prefix = GF_TO_TV_MAPPING.get(prefix, prefix)  # Default to the original prefix if not found in mapping
        return f"{tv_prefix}:{symbol}"
    except:
        return gf_ticker  # If there's any error, just return the original GF Ticker
