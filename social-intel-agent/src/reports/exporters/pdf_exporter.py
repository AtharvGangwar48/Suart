from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

class PDFExporter:
    def export_to_pdf(self, report_data: dict) -> BytesIO:
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        
        # Title
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "Social Intelligence Analysis Report")
        
        # Basic info
        p.setFont("Helvetica", 12)
        y_position = 700
        
        info_items = [
            f"Analysis ID: {report_data.get('analysis_id', 'N/A')}",
            f"Timestamp: {report_data.get('timestamp', 'N/A')}",
            f"URL: {report_data.get('url', 'N/A')}",
            f"Platform: {report_data.get('platform', 'N/A')}"
        ]
        
        for item in info_items:
            p.drawString(100, y_position, item)
            y_position -= 20
        
        # Risk assessment
        y_position -= 20
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, y_position, "Risk Assessment")
        y_position -= 20
        
        p.setFont("Helvetica", 12)
        risk_info = report_data.get('risk_assessment', {})
        risk_items = [
            f"Risk Level: {risk_info.get('level', 'N/A')}",
            f"Risk Score: {risk_info.get('score', 'N/A')}/10",
            f"Risk Factors: {', '.join(risk_info.get('factors', []))}"
        ]
        
        for item in risk_items:
            p.drawString(100, y_position, item)
            y_position -= 20
        
        # Summary
        y_position -= 20
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, y_position, "Summary")
        y_position -= 20
        
        p.setFont("Helvetica", 12)
        summary = report_data.get('summary', 'No summary available')
        p.drawString(100, y_position, summary)
        
        p.showPage()
        p.save()
        
        buffer.seek(0)
        return buffer