# Error Handling in Python
When writing code, one way or another you're going to run into errors. Some, you'll be able to fix by writing the code a little differently. In other cases, the error might be caused by a user or otherwise be invevitable. In these cases we need a way to deal with them so that the user isn't left with incomprehensible error messages.  
This is where error handling comes in.

## Try, except
In Python, the way to handle errors works a lot like an ``if``/``else`` statement. The keywords are ``try``, ``except``, ``else``, and ``finally``.  

Below is an example of trying to open a file. If ``orders.txt`` doesn't exist, the file in the ``except`` block is run. This is much more useful to the average user than a ``FileNotFoundError``.
```python
# (`try` and `except` block above)
else:
        # this only runs if the try didn't raise any exceptions
        # put data from file into a list
        orders = file.readlines()
            
        for i in range(len(orders)):
            orders[i] = orders[i].replace("\n", "") # remove the newline character

        print(orders) # print the orders

    finally:
        # always executes, regardless of errors
        print("I always run!")
```