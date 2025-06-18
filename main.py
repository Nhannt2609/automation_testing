import unittest
from utils.result_writer import write_results_to_excel

# Tìm tất cả test trong thư mục tests
loader = unittest.TestLoader()
suite = loader.discover("tests")

# Chạy tests
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# Ghi file Excel sau khi test xong
write_results_to_excel()