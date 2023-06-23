from django.db import models
from django.utils.text import slugify


# Create your models here.

class Country(models.Model):
    ID = models.AutoField(primary_key=True)
    ShortName = models.CharField(max_length=200)
    Currency = models.CharField(max_length=50)
    LongName = models.CharField(max_length=200)
    WHTRate = models.FloatField()
    OrdSeqNo = models.IntegerField()
    Alias1 = models.CharField(max_length=200, null=True, blank=True)
    Alias2 = models.CharField(max_length=200, null=True, blank=True)
    Adjective1 = models.CharField(max_length=200, null=True, blank=True)
    Adjective2 = models.CharField(max_length=200, null=True, blank=True)
    Adjective3 = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'country'
        
class Stock(models.Model):
    ID = models.AutoField(primary_key=True, db_column='ID')
    CountryID = models.IntegerField(db_column='CountryID')
    ReportType = models.CharField(max_length=200, db_column='ReportType')
    FinYearEnd = models.DateField(db_column='FinYearEnd')
    CompanyName = models.CharField(max_length=200, db_column='CompanyName')
    DisplayName = models.CharField(max_length=200, db_column='DisplayName')
    SEDOL = models.CharField(max_length=200, db_column='SEDOL')
    ISIN = models.CharField(max_length=200, db_column='ISIN')
    FTTicker = models.CharField(max_length=200, db_column='FTTicker')
    YFTicker = models.CharField(max_length=200, db_column='YFTicker')
    GFTicker = models.CharField(max_length=200, db_column='GFTicker')
    BBTicker = models.CharField(max_length=200, db_column='BBTicker')
    BCTicker = models.CharField(max_length=200, db_column='BCTicker')
    StockDescription = models.TextField(db_column='StockDescription')
    SPCurry = models.CharField(max_length=200, db_column='SPCurry')
    RefCurry = models.CharField(max_length=200, db_column='RefCurry')
    HighValue12mth = models.DecimalField(max_digits=19, decimal_places=4, db_column='12mthHighValue')
    LowValue12mth = models.DecimalField(max_digits=19, decimal_places=4, db_column='12mthLowValue')
    CurrentSharesOS = models.IntegerField(db_column='CurrentSharesOS')
    CurrentValue = models.DecimalField(max_digits=19, decimal_places=4, db_column='CurrentValue')
    CurrentDate = models.DateField(db_column='CurrentDate')
    MktCap = models.DecimalField(max_digits=19, decimal_places=4, db_column='MktCap')
    StockType = models.CharField(max_length=200, db_column='StockType')
    IndexID = models.IntegerField(db_column='IndexID')
    ISIN2 = models.CharField(max_length=200, db_column='ISIN2')
    StockURL = models.URLField(max_length=200, db_column='StockURL')
    slug = models.SlugField(max_length=500, blank=True)

    class Meta:
        managed = False
        db_table = 'stock'

    def _generate_slug(self):
        value = self.CompanyName
        slug_candidate = slugify(value, allow_unicode=True)
        unique_slug = slug_candidate
        num = 1
        while Stock.objects.filter(slug=unique_slug).exists():
            num += 1
            unique_slug = '{}-{}'.format(slug_candidate, num)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_slug()
        super().save(*args, **kwargs)    
        
        
class FinData(models.Model):
    ID = models.AutoField(primary_key=True)
    OrdSeqNo = models.IntegerField()
    FinDataName = models.CharField(max_length=255)
    FinDataType = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'findata'
        
class CoFinExport(models.Model):
    ID = models.AutoField(primary_key=True)
    StockID = models.ForeignKey('Stock', related_name='financial_data', db_column='StockID', on_delete=models.CASCADE)
    FinDataID = models.ForeignKey('FinData', db_column='FinDataID', on_delete=models.CASCADE)
    FinPerTypeID = models.IntegerField()
    PeriodEnd = models.DateField()
    RepCurry = models.CharField(max_length=255)
    RefCurry = models.CharField(max_length=255)
    RepDate = models.DateField()
    Multiplier = models.CharField(max_length=255)
    RepValue = models.FloatField()
    RefValue = models.FloatField()
    DataSource = models.CharField(max_length=255)
    Reliability = models.IntegerField()
    comment = models.TextField()
    PeriodEnd = models.DateField(db_index=True)


    class Meta:
        managed = False
        db_table = 'cofinexport'
        