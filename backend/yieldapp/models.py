# yieldapp/models.py

from django.db import models

# === TABEL PROSES UTAMA (14 PROSES) ===

class FormulationData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_formulation'

class FillingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_filling'

class InspectionData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_inspection'

class AssemblyData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_assembly'

class BlisteringData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_blistering'

class SecondaryPackagingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_secondary_packaging'

class ManualPackagingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_manual_packaging'

class ReinspectionData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_reinspection'

class FinalPackagingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_final_packaging'

class RejectSortingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_reject_sorting'

class WarehouseHandoverData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_warehouse_handover'

class PrimaryPackagingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_primary_packaging'

class RetestingData(models.Model):
    batch_number = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    production_line = models.CharField(max_length=50)
    process_date = models.DateField()
    output_value = models.DecimalField(max_digits=20, decimal_places=2)
    yield_percent = models.DecimalField(max_digits=5, decimal_places=2)
    loss = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    qc_sample = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    action_plan = models.TextField(null=True, blank=True)
    issue = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'kalbio_yield_retesting'

# === OLAP VIEW ===

class FinalYieldSummary(models.Model):
    batch_number = models.CharField(max_length=50, primary_key=True)
    product = models.CharField(max_length=100)
    formulation_output = models.DecimalField(max_digits=20, decimal_places=2)
    filling_output = models.DecimalField(max_digits=20, decimal_places=2)
    inspection_output = models.DecimalField(max_digits=20, decimal_places=2)
    assembly_output = models.DecimalField(max_digits=20, decimal_places=2)
    blistering_output = models.DecimalField(max_digits=20, decimal_places=2)
    packaging_output = models.DecimalField(max_digits=20, decimal_places=2)
    final_output = models.DecimalField(max_digits=20, decimal_places=2)
    final_yield_percent = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'yield_summary_view'
