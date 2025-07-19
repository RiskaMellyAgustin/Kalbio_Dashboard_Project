from yieldapp.models import FinalYieldSummary
from django.db.models import Avg, Sum
from collections import defaultdict

def get_final_yield_trend():
    data = FinalYieldSummary.objects.order_by('batch_date')
    return [
        {"label": item.batch_date.strftime('%Y-%m-%d'), "value": float(item.final_yield)}
        for item in data
    ]

def get_waterfall_loss():
    total = FinalYieldSummary.objects.aggregate(
        loss_filling=Sum('loss_filling'),
        loss_inspection=Sum('loss_inspection'),
        loss_assembly=Sum('loss_assembly'),
        loss_blistering=Sum('loss_blistering'),
        loss_packaging_manual=Sum('loss_packaging_manual'),
        qc_sample=Sum('qc_sample'),
        yield_loss=Sum('yield_loss'),
    )
    return [
        {"label": key.replace('_', ' ').title(), "value": float(value or 0)}
        for key, value in total.items()
    ]

def get_yield_per_batch():
    data = FinalYieldSummary.objects.order_by('batch_no')
    return [
        {"label": item.batch_no, "value": float(item.final_yield)}
        for item in data
    ]
