from django.db import models

# Create your models here.


class TradeFormDetails(models.Model):
    date_time=models.DateTimeField()
    asset=models.CharField(max_length=255)
    direction=models.CharField(max_length=255)
    entry_price=models.DecimalField(max_digits=10,decimal_places=2)
    exit_price=models.DecimalField(max_digits=10,decimal_places=2)
    loat_size=models.DecimalField(max_digits=10,decimal_places=4)
    risk_manage=models.DecimalField(max_digits=10,decimal_places=3)
    trade_result=models.CharField(max_length=200)

    reason_for_trade=models.CharField(max_length=255)


    emotions=models.CharField(max_length=255)
   
    you_learned=models.CharField(max_length=255,null=True,blank=True)	
    screenshot=models.ImageField(upload_to='media',null=True,blank=True)

    def __str__(self):
        return f"{self.asset} trade on {self.date_time.strftime('%Y-%m-%d')}"
