from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.TextField()
    company = models.CharField(max_length=200)
    adress = models.TextField()


class Mission(models.Model):
    customer = models.ForeignKey(Customer,
                               on_delete=models.CASCADE,
                               related_name='mission_client')
    category = models.CharField(max_length=50,
                                choices=[('COACHING', 'COACHING'),
                                         ('CONSEIL', 'CONSEIL'),
                                         ('FORMATION', 'FORMATION')])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    qualiopi = models.BooleanField(default=False)
    price = models.FloatField()
    costs = models.BooleanField(default=False)
    if costs is True:
        costs_list = models.TextField()


class Estimate(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 related_name='estimate_customer')
    mission = models.ForeignKey(Mission,
                                on_delete=models.CASCADE,
                                related_name='estimate_mission')
    

class Contract(models.Model):
    estimate = models.ForeignKey(Estimate,
                                on_delete=models.CASCADE,
                                related_name='contract_estimate')


class Invoice(models.Model):
    contract = models.ForeignKey(Contract,
                                 on_delete=models.CASCADE,
                                 related_name='invoice_contract')
