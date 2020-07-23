'''
    
'''
from    collections import  OrderedDict 

class NNObj (
    ):
    '''An object that never returns None (Never None Obj).

        `NNObj` behavior tries to memmic the behavior of the coalescing operator `?` or `??` in other languages. 

        Example:
            >>> from salobj import NNObj
            >>> class A(NNObj):
            >>>     def __init__(self):
            >>>         self.va  = 'VA'
            >>>         self.vb  = None
            >>>     def fa(self):
            >>>         return 'VFA'
            >>>     def fb(self):
            >>>         return None
            >>> a = A()
            >>> #'A' object has not attribute 'c', new `NNObj` is returned instead 
            >>> a.c
                <salobj.objs.NNObj at 0x????>
            >>> a.c().d.e.f(a = 1)
                <salobj.objs.NNObj at 0x????>
            >>> a.va
                'VA'
            >>> a.vb
                <salobj.objs.NNObj at 0x????>
            >>> a.fa()
                'VFA'
            >>> a.fb()
                <salobj.objs.NNObj at 0x????>
            >>> a.vb.do_something(x= 1, y= 2)
                <salobj.objs.NNObj at 0x????>
    '''
    def _wrapper            (
        #
                self        ,
                function    ,
            ):
        def __wrapper   (
            #
                    *args       ,
                    **kwargs    ,
                ):
            
            value   = function(*args, **kwargs)
            return value if value != None else NNObj()

        return __wrapper

    def __call__            (
        #
                self        ,
                *args       ,
                **kwargs    ,
            ):
        return NNObj()
    def __getattribute__    (
        #
                self    ,
                name    ,
            ):
        value   = object.__getattribute__(self, name)
        if      value == None           : return NNObj()
        elif    callable(value)         : return value if getattr(value, '__name__', '') == '_wrapper' else self._wrapper(value)
        else                            : return value
    def __getattr__         (
        #
                self    , 
                name    ,
            ):
        return NNObj()