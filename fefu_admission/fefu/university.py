import os

from fefu_admission.university.university.university import University
from fefu_admission.university.settings import Settings
from .department import FefuDepartment


class FefuUniversity(University):

    def __init__(self):
        super().__init__()
        self.name = "ДВФУ"
        self.departments = []
        self.data_path = os.path.join(os.path.expanduser('~'), ".fefu_admission")
        self.settings = Settings(self)
        for department in self.settings.list_of_departments:
            self.departments.append(FefuDepartment(department, self))