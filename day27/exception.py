try:
    a = int(input())
    k={1:12,2:13}
    print(k[14])
    l=[234,56]
    print(l[10])
    print('l'+1)
except ValueError:
    print("Enter the correct datavalue")
except KeyError:
    print("Key is not there")
except ZeroDivisionError:
    print("Can't divide with Zero")
except IndexError:
    print("Index out of range")  
except TypeError:
    print("Enter the correct datatype")
except NameError:
    print("define the variable")
else:
    print("Error free program")
finally:
    print("End of the program")

except (ValueError,KeyError,ZeroDivisionError,IndexError,TypeError,NameError):