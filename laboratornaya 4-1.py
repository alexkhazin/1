def counter(func):
  
    func.inv_count_ = 0

    def wrapper(*args, **kwargs):
        func.inv_count_ += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, func.inv_count_ ))
        return res
    
   return wrapper
   @counter
   def foo(a,b)
        return a+b
    foo(3,4)
    foo(5,6)
    foo(10,22)
    
