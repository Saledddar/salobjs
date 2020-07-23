'''Test for salobj.objs
'''
from    salobj.objs import  NNObj  

import  pytest 

class TestNNObj (
    ):
    def test_basic                  (
        #Expected basic behavior
                self    ,
            ):
        nn_obj  = NNObj()
        
        assert  type(nn_obj.a)      == NNObj
        assert  type(nn_obj.a.b())  == NNObj
    def test_function_args_kwargs   (
        #Function calls with args and kwargs
                self    ,
            ):
        nn_obj      = NNObj()
        nn_obj.va   = 'VA'
        nn_obj.vb   = None
        nn_obj.fa   = lambda        : 'VFA'
        nn_obj.fb   = lambda        : None
        nn_obj.fc   = lambda x, y   : x+y

        assert  type(nn_obj.a.b(1,2,3).c(a= 1, b= 2))   == NNObj
        assert  nn_obj.va                               == 'VA'
        assert  nn_obj.fa()                             == 'VFA'
        assert  nn_obj.fc(1,2)                          == 3
        assert  type(nn_obj.vb.c.d())                   == NNObj
        assert  type(nn_obj.fb().va)                    == NNObj
    def test_inheritance            (
        #Behavior on inheritance
                self    ,
            ):
        class A (
            #
                    NNObj   ,   
                ):
            def fa  (
                #
                        self    ,
                    ):
                return 'VFA'
                
            def __init__    (
                #
                        self    ,
                    ):
                self.va  = 'VA'

        a_nn_obj    = A()

        assert  a_nn_obj.fa()           == 'VFA'
        assert  a_nn_obj.va             == 'VA'
        assert  type(a_nn_obj.c.d.e)    == NNObj
    def test_change_behavior        (
        #Changing the behavior of an existing class 
                self    ,
            ):
        class A (
            ):
            def fa  (
                #
                        self    ,
                    ):
                return 'VFA'
            def fb  (
                #
                        self    ,
                    ):
                return None
            
            def __init__    (
                #
                        self    ,
                    ):
                self.va  = 'VA'
        class NNA   (
            #
                    A       ,
                    NNObj   ,
                ):
            pass
        
        a_nn_obj    = NNA()
        
        assert  a_nn_obj.fa()           == 'VFA'
        assert  a_nn_obj.va             == 'VA'
        assert  type(a_nn_obj.fb())     == NNObj
        assert  type(a_nn_obj.c.d.e)    == NNObj
        
