# backend/yieldapp/views.py

import csv
from django.shortcuts import render
from django.contrib import messages
from .models import FormulationData  # pastikan model ini udah kamu buat
from datetime import datetime

def upload_csv(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File bukan CSV!')
            return render(request, "upload.html")

        file_data = csv_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(file_data)

        for row in reader:
            FormulationData.objects.create(
                batch_number=row["batch_number"],
                product=row["product"],
                date=datetime.strptime(row["date"], "%Y-%m-%d"),
                output_value=float(row["output_value"])
            )

        messages.success(request, "Data berhasil diupload!")
        return render(request, "upload.html")

    return render(request, "upload.html")

from django.shortcuts import render

def dashboard_operator(request):
    return render(request, 'dashboard_operator.html')  # pastikan template ini ada


# yieldapp/views.py
from django.shortcuts import render, redirect
from .forms import UploadCSVForm
from .services import cleaning

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            process = form.cleaned_data['process_type']
            file = request.FILES['file']
            cleaning.handle_csv_upload(file, process)
            return render(request, 'upload.html', {'form': form, 'success': True})
    else:
        form = UploadCSVForm()
    return render(request, 'upload.html', {'form': form})

from django.shortcuts import render
from .services.dashboard_charts import (
    get_final_yield_trend,
    get_waterfall_loss,
    get_yield_per_batch
)

def dashboard_mstd(request):
    yield_trend = get_final_yield_trend()
    waterfall_data = get_waterfall_loss()
    batch_yield = get_yield_per_batch()
    
    return render(request, 'dashboard_mstd.html', {
        'yield_trend': yield_trend,
        'waterfall_data': waterfall_data,
        'batch_yield': batch_yield,
    })

