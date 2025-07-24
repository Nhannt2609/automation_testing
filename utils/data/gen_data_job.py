from faker import Faker

fake = Faker()

def generate_job_data(include_optional=True):
    data = {
        "vessel": fake.word(),
        "eta": "2025-08-01",
        "job_type": "IMPORT",
    }
    if include_optional:
        data["description"] = fake.text()
    return data