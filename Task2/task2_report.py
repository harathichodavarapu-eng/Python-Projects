# Task 2: Automated Report Generation
# Generates a simple PDF report

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Automated Report", ln=True)
pdf.cell(200, 10, txt="This is a sample report.", ln=True)
pdf.cell(200, 10, txt="Task completed successfully.", ln=True)

pdf.output("task2_report.pdf")