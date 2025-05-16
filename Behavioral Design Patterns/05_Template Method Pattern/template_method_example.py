"""
Template Method Design Pattern Example in Python
------------------------------------------------
This example demonstrates a basic report generation system where different types of reports
share the same structure: fetch data -> process data -> generate report.
The abstract class defines the template and leaves the data processing to subclasses.
"""

from abc import ABC, abstractmethod

class ReportTemplate(ABC):
    """
    Abstract base class (Template)
    Defines the algorithm's skeleton and leaves the custom steps to subclasses.
    """

    def generate_report(self):
        """
        The template method that defines the steps of the algorithm.
        This should not be overridden.
        """
        self.fetch_data()
        self.process_data()
        self.export_report()

    def fetch_data(self):
        """
        Concrete method: Step 1 - Common logic to fetch data (can be shared).
        """
        print("Fetching data from database...")

    @abstractmethod
    def process_data(self):
        """
        Abstract method: Step 2 - To be defined in subclass.
        Each subclass will have its own way to process data.
        """
        pass

    def export_report(self):
        """
        Hook method: Step 3 - Optional customization for exporting.
        Can be overridden but not required.
        """
        print("Exporting report as PDF.")


class SalesReport(ReportTemplate):
    """
    Concrete class that implements data processing specific to Sales Reports.
    """

    def process_data(self):
        print("Processing sales data: calculating revenue, growth...")


class InventoryReport(ReportTemplate):
    """
    Concrete class that implements data processing specific to Inventory Reports.
    """

    def process_data(self):
        print("Processing inventory data: checking stock levels, reorder points...")

    def export_report(self):
        # Optionally override the hook method
        print("Exporting inventory report as Excel file.")


if __name__ == "__main__":
    print("\n--- Generating Sales Report ---")
    sales = SalesReport()
    sales.generate_report()

    print("\n--- Generating Inventory Report ---")
    inventory = InventoryReport()
    inventory.generate_report()
