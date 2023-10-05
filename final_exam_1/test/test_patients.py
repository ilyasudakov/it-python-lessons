import re
from playwright.sync_api import Page, expect

from conftest import authenticated_page

from pages.patients import PatientDetailsPage


def test_patient_details_page_has_title(authenticated_page):
    details_page = PatientDetailsPage(authenticated_page)

    details_page.navigate()

    assert details_page.title == "Patient details"


def test_patient_details_page_redirect_to_admin(authenticated_page):
    details_page = PatientDetailsPage(authenticated_page)

    details_page.navigate()

    details_page.edit_patient()

    assert (
        details_page.title == "Patient object (8) | Change patient | Django site admin"
    )
