from openpyxl import Workbook
from datetime import datetime
import time

results = []

def record_result(name, status, start_time, error=None):
    duration = round(time.time() - start_time, 2)
    results.append({
        "Test Case": name,
        "Status": status,
        "Time (s)": duration,
        "Error Detail": error or "",
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def write_results_to_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Test Results"
    ws.append(["Test Case", "Status", "Time (s)", "Error Detail", "Timestamp"])

    for res in results:
        ws.append([res["Test Case"], res["Status"], res["Time (s)"], res["Error Detail"], res["Timestamp"]])

    filename = f"logs/test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)
    print(f"✅ Đã ghi kết quả vào file Excel: {filename}")