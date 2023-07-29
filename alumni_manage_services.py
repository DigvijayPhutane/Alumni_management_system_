from abc  import ABC,abstractmethod

class Alumni_Management_Services(ABC):

    @abstractmethod
    def add_alumni(self):
        pass
    @abstractmethod
    def delete_alumni(self):
        pass
    @abstractmethod
    def search_alumni(self):
        pass
    @abstractmethod
    def list_alumni(self):
        pass
    @abstractmethod
    def alumni_of_year_in_range(self):
        pass
    @abstractmethod
    def export_data_excel(self):
        pass
    @abstractmethod
    def import_excel_data(self):
        pass