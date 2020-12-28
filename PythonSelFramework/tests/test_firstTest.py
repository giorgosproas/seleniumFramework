from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_demo1(self):
        log = self.getLogger()
        log.info("demo1")
        assert 1==1
        
    def test_demo2(self):
        log = self.getLogger()
        log.info("demo2")
        assert 1==1