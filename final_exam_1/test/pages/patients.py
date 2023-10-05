class PatientDetailsPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://localhost:8000/patients"
        self.edit_patient_button = page.get_by_text("Edit")

    @property
    def title(self):
        return self.page.title()

    def navigate(self):
        self.page.goto(f"{self.url}/8")

    def edit_patient(self):
        """Click on the Edit button. Redirects to the /admin/patients/:id"""
        self.edit_patient_button.click()
