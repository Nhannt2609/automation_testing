import unittest

# Tìm tất cả test trong thư mục tests
loader = unittest.TestLoader()
suite = loader.discover("tests")

# Chạy tests
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)