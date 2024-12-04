import csv
from flask import Response

def export_to_csv(data, filename='export.csv'):
    def generate():
        writer = csv.writer()
        writer.writerow(data[0].keys())  # Write headers
        for row in data:
            writer.writerow(row.values())
        yield writer.getvalue()

    return Response(generate(), mimetype='text/csv', headers={"Content-Disposition": f"attachment;filename={filename}"})
