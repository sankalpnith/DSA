class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

log = Logger()



class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance

Logger.get_instance()


# java

public class SingletonClass {
    private static final SingletonClass SINGLE_INSTANCE = null;
    private SingletonClass() {}
  public static SingletonClass getInstance() {
      if SINGLE_INSTANCE == null:
          Single_INSTANCE = new SingletonClass();
      return Single_INSTANCE;
    }
}