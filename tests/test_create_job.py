import pytest
# from pages.jobs_page import JobsPage
# from utils.data_generator import generate_job_data

class TestCreateJob:

    def test_001_create_job_with_all_fields(self, driver):
        job_data = generate_job_data(include_optional=True)
        job_page = JobsPage(driver)
        job_page.create_job(job_data)
        assert job_page.is_job_created_successfully()

    def test_002_create_job_missing_required_field(self, driver):
        job_data = generate_job_data(include_optional=False)
        job_data["vessel"] = ""  # Bỏ trống field bắt buộc
        job_page = JobsPage(driver)
        job_page.create_job(job_data)
        assert job_page.has_error("vessel is a required field")