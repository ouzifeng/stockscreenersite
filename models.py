# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cagr(models.Model):
    stockid = models.BigIntegerField(db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    revenue_cagr = models.FloatField(db_column='Revenue CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    op_inc_cagr = models.FloatField(db_column='Op Inc CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    net_inc_exc_ext_cagr = models.FloatField(db_column='Net Inc exc ext CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_cagr = models.FloatField(db_column='EPS CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_cagr = models.FloatField(db_column='Dividend CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cashops_cagr = models.FloatField(db_column='CashOps CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capex_cagr = models.FloatField(db_column='Capex CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    equity_cagr = models.FloatField(db_column='Equity CAGR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyback_ratio = models.FloatField(db_column='buyback ratio', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    goodwill_total_equity = models.FloatField(db_column='goodwill/total equity', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    roburm = models.FloatField(db_column='RoburM', blank=True, null=True)  # Field name made lowercase.
    enterprise_ratio = models.FloatField(db_column='Enterprise ratio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eqps_price = models.FloatField(db_column='EqPS/Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price_hilo = models.FloatField(db_column='Price/HiLo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_e = models.FloatField(db_column='P/E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yield_field = models.FloatField(db_column='Yield %', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    peg_ratio = models.FloatField(db_column='PEG Ratio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'cagr'


class Cofinexport(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    stockid = models.BigIntegerField(db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    findataid = models.BigIntegerField(db_column='FinDataID', blank=True, null=True)  # Field name made lowercase.
    finpertypeid = models.BigIntegerField(db_column='FinPerTypeID', blank=True, null=True)  # Field name made lowercase.
    periodend = models.DateTimeField(db_column='PeriodEnd', blank=True, null=True)  # Field name made lowercase.
    repcurry = models.TextField(db_column='RepCurry', blank=True, null=True)  # Field name made lowercase.
    refcurry = models.TextField(db_column='RefCurry', blank=True, null=True)  # Field name made lowercase.
    repdate = models.DateTimeField(db_column='RepDate', blank=True, null=True)  # Field name made lowercase.
    multiplier = models.TextField(db_column='Multiplier', blank=True, null=True)  # Field name made lowercase.
    repvalue = models.FloatField(db_column='RepValue', blank=True, null=True)  # Field name made lowercase.
    refvalue = models.FloatField(db_column='RefValue', blank=True, null=True)  # Field name made lowercase.
    datasource = models.TextField(db_column='DataSource', blank=True, null=True)  # Field name made lowercase.
    reliability = models.FloatField(db_column='Reliability', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cofinexport'


class Country(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='ShortName', blank=True, null=True)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    longname = models.TextField(db_column='LongName', blank=True, null=True)  # Field name made lowercase.
    whtrate = models.BigIntegerField(db_column='WHTRate', blank=True, null=True)  # Field name made lowercase.
    ordseqno = models.BigIntegerField(db_column='OrdSeqNo', blank=True, null=True)  # Field name made lowercase.
    alias1 = models.TextField(db_column='Alias1', blank=True, null=True)  # Field name made lowercase.
    alias2 = models.FloatField(db_column='Alias2', blank=True, null=True)  # Field name made lowercase.
    adjective1 = models.TextField(db_column='Adjective1', blank=True, null=True)  # Field name made lowercase.
    adjective2 = models.TextField(db_column='Adjective2', blank=True, null=True)  # Field name made lowercase.
    adjective3 = models.FloatField(db_column='Adjective3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class CountryBloc(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    countryid = models.BigIntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    blocid = models.BigIntegerField(db_column='BlocID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country_bloc'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Findata(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    ordseqno = models.BigIntegerField(db_column='OrdSeqNo', blank=True, null=True)  # Field name made lowercase.
    findataname = models.TextField(db_column='FinDataName', blank=True, null=True)  # Field name made lowercase.
    findatatype = models.TextField(db_column='FinDataType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'findata'


class Finpertype(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    finpertypename = models.TextField(db_column='FinPerTypeName', blank=True, null=True)  # Field name made lowercase.
    duration = models.BigIntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finpertype'


class Forex(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.TextField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    currya = models.TextField(db_column='CurryA', blank=True, null=True)  # Field name made lowercase.
    curryb = models.TextField(db_column='CurryB', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forex'


class MyappCofinexport(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    finpertypeid = models.IntegerField(db_column='FinPerTypeID')  # Field name made lowercase.
    periodend = models.DateField(db_column='PeriodEnd')  # Field name made lowercase.
    repcurry = models.CharField(db_column='RepCurry', max_length=255)  # Field name made lowercase.
    refcurry = models.CharField(db_column='RefCurry', max_length=255)  # Field name made lowercase.
    repdate = models.DateField(db_column='RepDate')  # Field name made lowercase.
    multiplier = models.CharField(db_column='Multiplier', max_length=255)  # Field name made lowercase.
    repvalue = models.FloatField(db_column='RepValue')  # Field name made lowercase.
    refvalue = models.FloatField(db_column='RefValue')  # Field name made lowercase.
    datasource = models.CharField(db_column='DataSource', max_length=255)  # Field name made lowercase.
    reliability = models.IntegerField(db_column='Reliability')  # Field name made lowercase.
    comment = models.TextField()
    findataid = models.ForeignKey('MyappFindata', models.DO_NOTHING, db_column='FinDataID')  # Field name made lowercase.
    stockid = models.ForeignKey('Stock', models.DO_NOTHING, db_column='StockID_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'myapp_cofinexport'


class MyappFindata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordseqno = models.IntegerField(db_column='OrdSeqNo')  # Field name made lowercase.
    findataname = models.CharField(db_column='FinDataName', max_length=255)  # Field name made lowercase.
    findatatype = models.CharField(db_column='FinDataType', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'myapp_findata'


class Sector(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    secgrpid = models.BigIntegerField(db_column='SecGrpID', blank=True, null=True)  # Field name made lowercase.
    sectorname = models.TextField(db_column='SectorName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sector'


class Sectorgroup(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    secgrpname = models.TextField(db_column='SecGrpName', blank=True, null=True)  # Field name made lowercase.
    secgrpalias = models.FloatField(db_column='SecGrpAlias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectorgroup'


class Stock(models.Model):
    id = models.BigIntegerField(db_column='ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    countryid = models.BigIntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    reporttype = models.FloatField(db_column='ReportType', blank=True, null=True)  # Field name made lowercase.
    finyearend = models.TextField(db_column='FinYearEnd', blank=True, null=True)  # Field name made lowercase.
    companyname = models.TextField(db_column='CompanyName', blank=True, null=True)  # Field name made lowercase.
    displayname = models.TextField(db_column='DisplayName', blank=True, null=True)  # Field name made lowercase.
    sedol = models.TextField(db_column='SEDOL', blank=True, null=True)  # Field name made lowercase.
    isin = models.TextField(db_column='ISIN', blank=True, null=True)  # Field name made lowercase.
    ftticker = models.TextField(db_column='FTTicker', blank=True, null=True)  # Field name made lowercase.
    yfticker = models.TextField(db_column='YFTicker', blank=True, null=True)  # Field name made lowercase.
    gfticker = models.TextField(db_column='GFTicker', blank=True, null=True)  # Field name made lowercase.
    bbticker = models.TextField(db_column='BBTicker', blank=True, null=True)  # Field name made lowercase.
    bcticker = models.TextField(db_column='BCTicker', blank=True, null=True)  # Field name made lowercase.
    stockdescription = models.TextField(db_column='StockDescription', blank=True, null=True)  # Field name made lowercase.
    spcurry = models.TextField(db_column='SPCurry', blank=True, null=True)  # Field name made lowercase.
    refcurry = models.TextField(db_column='RefCurry', blank=True, null=True)  # Field name made lowercase.
    number_12mthhighvalue = models.FloatField(db_column='12mthHighValue', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12mthlowvalue = models.FloatField(db_column='12mthLowValue', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    currentsharesos = models.FloatField(db_column='CurrentSharesOS', blank=True, null=True)  # Field name made lowercase.
    currentvalue = models.FloatField(db_column='CurrentValue', blank=True, null=True)  # Field name made lowercase.
    currentdate = models.TextField(db_column='CurrentDate', blank=True, null=True)  # Field name made lowercase.
    mktcap = models.FloatField(db_column='MktCap', blank=True, null=True)  # Field name made lowercase.
    stocktype = models.FloatField(db_column='StockType', blank=True, null=True)  # Field name made lowercase.
    indexid = models.FloatField(db_column='IndexID', blank=True, null=True)  # Field name made lowercase.
    isin2 = models.FloatField(db_column='ISIN2', blank=True, null=True)  # Field name made lowercase.
    stockurl = models.TextField(db_column='StockURL', blank=True, null=True)  # Field name made lowercase.
    slug = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class StockSector(models.Model):
    id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    stockid = models.BigIntegerField(db_column='StockID', blank=True, null=True)  # Field name made lowercase.
    sectorid = models.BigIntegerField(db_column='SectorID', blank=True, null=True)  # Field name made lowercase.
    level = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_sector'
