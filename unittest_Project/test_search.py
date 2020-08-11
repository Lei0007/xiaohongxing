import unittest
# 被测试方法
class Search:
    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.search = Search()

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("是否相等")
        self.assertEquals(1, 1, "判断1 ==1")
    def test_notequal(self):
        print("是否必相等")
        self.assertNotEqual(1,89, "判断1 ！= 3")

if __name__ == '__main__':
    # 执行当前文件的unittest测试用例
    '''unittest.main()'''
# 创建一个测试套件,testsuite,
# 执行指定的测试用例,将执行的测试用例添加到测试套件里面,批量执行
suite = unittest.TestSuite()
suite.addTest(TestSearch("test_search1"))
unittest.TextTestRunner().run(suite)

# 执行某个测试类
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
suite = unittest.TestSuite([suite1])
unittest.TextTestRunner(verbosity=2).run(suite)