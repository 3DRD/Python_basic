# Packages
# when importing from packages  can either use
#
# from package_name.module_name import function_name/class_name
# In case of class we have to create objects
# OR
# from package_name import module_name ,
# then we need to use functions as module_name.function_name

# from ecommerece.shipping import calculate_ship
from ecommerece import shipping

shipping.calculate_ship()
