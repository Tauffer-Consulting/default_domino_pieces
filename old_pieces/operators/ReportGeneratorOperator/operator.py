from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel

import os
import time
from fpdf import FPDF


class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')


class ReportGeneratorOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        ########## Operator task ##########
        # Create PDF
        pdf = PDF() # A4 (210 by 297 mm)

        # Add First page
        pdf.add_page()
        self.create_title("FlowUI Report", pdf)

        for task in os.listdir(self.run_path):
            # Add Page
            pdf.add_page()
            self.create_sub_title(task, pdf)

            # Add text to PDF
            for file in os.listdir(f'{self.run_path}/{task}/report'):
                if file.endswith('.txt'):
                    with open(file, 'r') as f:
                        text_task = f.read()

                    self.write_to_pdf(pdf, text_task)
                    pdf.ln(15)

            # Add figure to PDF
            for file in os.listdir(f'{self.run_path}/{task}/report'):
                if file.endswith('.png'):
                    pdf.image(file, w=200)
                    pdf.ln(10)

        # Generate the PDF
        pdf.output(f"{self.run_path}/report.pdf", 'F')
 
        return OutputModel(
            message="Report generated successfully!"
        )

    
    def generate_report(self):
        self._logger.info("Report generated successfully!")
    

    def create_title(self, title, pdf):
        # Add main title
        pdf.set_font('Helvetica', 'b', 20)  
        pdf.ln(40)
        pdf.write(5, title)
        pdf.ln(10)
        
        # Add date of report
        pdf.set_font('Helvetica', '', 14)
        pdf.set_text_color(r=128,g=128,b=128)
        today = time.strftime("%d/%m/%Y")
        pdf.write(4, f'{today}')
        pdf.ln(10)


    def create_sub_title(self, title, pdf):
        pdf.set_font('Helvetica', 'b', 14)
        pdf.write(5, title)
        pdf.ln(10)


    def write_to_pdf(self, pdf, words):        
        # Set text colour, font size, and font type
        pdf.set_text_color(r=0,g=0,b=0)
        pdf.set_font('Helvetica', '', 12)
        pdf.write(5, words)
