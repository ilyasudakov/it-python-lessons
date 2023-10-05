import re
from playwright.sync_api import Page, expect

from pages.patient_details import PatientDetailsPage


def test_has_title(page: Page):
    details_page = PatientDetailsPage(page)

    details_page.navigate()

    assert details_page.title == "Patient details"
