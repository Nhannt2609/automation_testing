# import unittest
# # from utils.result_writer import write_results_to_excel

# # Tìm tất cả test trong thư mục tests
# loader = unittest.TestLoader()
# suite = loader.discover("tests")

# # Chạy tests
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(suite)

# Ghi file Excel sau khi test xong
# write_results_to_excel()

import unittest
from tests.test_create_job import CreateJobTest

if __name__ == "__main__":
    for i in range(5):
        print(f"\n🔁 Lần chạy thứ {i+1}")
        suite = unittest.TestLoader().loadTestsFromTestCase(CreateJobTest)
        unittest.TextTestRunner().run(suite)