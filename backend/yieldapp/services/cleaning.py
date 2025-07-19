# yieldapp/services/cleaning.py
import pandas as pd
from io import TextIOWrapper
from ..models import (
    FillingData, InspectionData, AssemblyData, BlisteringData,
    FinalPackagingData, WarehouseHandoverData
)

def handle_csv_upload(file, process):
    df = pd.read_csv(TextIOWrapper(file, encoding='utf-8'))
    model_map = {
        'filling': FillingData,
        'inspection': InspectionData,
        'assembly': AssemblyData,
        'blistering': BlisteringData,
        'packaging': FinalPackagingData,
        'handover': WarehouseHandoverData,
    }
    model = model_map.get(process)
    if model:
        for _, row in df.iterrows():
            model.objects.create(**row.to_dict())
