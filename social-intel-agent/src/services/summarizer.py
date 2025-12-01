from src.reports.builder import ReportBuilder

class Summarizer:
    def __init__(self):
        self.report_builder = ReportBuilder()
    
    def generate_report(self, content: dict, risk_score: dict):
        return self.report_builder.build_report(content, risk_score)