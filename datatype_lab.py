import unittest

def data_type(data):
  if  isinstance(data, int):
    if data<100:
      return 'less than 100'
    elif data>100:
      return 'more than 100'
    elif data==100:
     return 'equal to 100'
    else:
      pass
  
  elif isinstance(data, str):
    return len(data)
  elif data is bool:
    return bool
  elif data is None:
    return 'no value'
    
  else:
    pass


#tests
class DataTypeTestCase(TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))
  
  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))

