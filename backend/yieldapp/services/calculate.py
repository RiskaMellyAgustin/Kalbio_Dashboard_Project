# services/calculate.py

def calculate_final_yield(output_qty, input_qty):
    if input_qty == 0:
        return 0
    return round((output_qty / input_qty) * 100, 2)

def calculate_loss(input_qty, output_qty):
    if input_qty == 0:
        return 0
    return input_qty - output_qty

def calculate_yield_loss_percentage(input_qty, output_qty):
    if input_qty == 0:
        return 0
    return round(((input_qty - output_qty) / input_qty) * 100, 2)

def calculate_qc_sample_loss(qc_sample_qty):
    return qc_sample_qty

def calculate_total_losses(*losses):
    return sum(losses)

def calculate_yield_metrics(row):
    """
    row: dict dari CSV
    return: dict hasil hitung metric (losses, yield final, dll)
    """
    try:
        input_ = float(row.get("input", 0))
        output = float(row.get("output", 0))
        qc_sample = float(row.get("qc_sample", 0))
        reject = float(row.get("reject", 0))
    except ValueError:
        return {}

    loss = calculate_loss(input_, output)
    yield_percent = calculate_final_yield(output, input_)
    yield_loss_percent = calculate_yield_loss_percentage(input_, output)
    qc_loss = calculate_qc_sample_loss(qc_sample)
    total_loss = calculate_total_losses(loss, qc_loss, reject)

    return {
        "input": input_,
        "output": output,
        "qc_sample": qc_sample,
        "reject": reject,
        "loss": loss,
        "yield_percent": yield_percent,
        "yield_loss_percent": yield_loss_percent,
        "qc_loss": qc_loss,
        "total_loss": total_loss
    }
