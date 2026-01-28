import pandas as pd
from fpdf import FPDF
import os
from datetime import datetime

# REAL WORLD SCENARIO: Finance Automation
# "We have a CSV of monthly sales. We need to generate a PDF invoice for each customer instantly."
# This simulates a very common back-office task.

def generate_invoice_data():
    """Creates dummy data for the example"""
    data = {
        'InvoiceID': ['INV-1001', 'INV-1002', 'INV-1003'],
        'CustomerName': ['Acme Corp', 'Wayne Enterprises', 'Stark Industries'],
        'Item': ['Consulting Services', 'Software License', 'Cloud Hosting'],
        'Amount': [5000.00, 12000.50, 850.75],
        'Date': ['2024-01-15', '2024-01-16', '2024-01-17']
    }
    df = pd.DataFrame(data)
    df.to_csv('monthly_orders.csv', index=False)
    print("Generated 'monthly_orders.csv'")

class PDF(FPDF):
    def header(self):
        # Logo placeholder
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'INVOICE', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_invoice(order):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Invoice Details
    pdf.cell(200, 10, txt=f"Invoice ID: {order['InvoiceID']}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {order['Date']}", ln=True)
    pdf.ln(10) # Line break
    
    # Customer Details
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt=f"Bill To: {order['CustomerName']}", ln=True)
    pdf.ln(10)
    
    # Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(100, 10, "Description", 1, 0, 'C', 1)
    pdf.cell(50, 10, "Amount (USD)", 1, 1, 'C', 1)
    
    # Table Content
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, str(order['Item']), 1)
    pdf.cell(50, 10, f"${order['Amount']:.2f}", 1, 1, 'R')
    
    # Total
    pdf.ln(5)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(100, 10, "Total", 0, 0, 'R')
    pdf.cell(50, 10, f"${order['Amount']:.2f}", 1, 1, 'R')
    
    # Ensure folder exists
    if not os.path.exists("invoices"):
        os.makedirs("invoices")
        
    filename = f"invoices/{order['InvoiceID']}_{order['CustomerName'].replace(' ', '_')}.pdf"
    pdf.output(filename)
    print(f"Generated: {filename}")

def main():
    if not os.path.exists('monthly_orders.csv'):
        generate_invoice_data()
    
    df = pd.read_csv('monthly_orders.csv')
    
    print("Starting Batch Invoice Generation...")
    for index, row in df.iterrows():
        create_invoice(row)
    print("Batch processing complete.")

if __name__ == "__main__":
    # Requirement: pip install pandas fpdf
    main()
