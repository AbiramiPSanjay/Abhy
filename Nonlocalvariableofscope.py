def outer():
  msg="Local"
  def inner():
    msg="Non-Local"
    print("inner=",msg)
    inner()
  print("outer:",msg)
outer()    
