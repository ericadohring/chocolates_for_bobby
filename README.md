# Order Processor for a fictional small business Bobby's Chocolates

A lightweight CLI order processor for fictional business "Bobby's Chocolates."

_Input_: CSV file. Each line represents an order
```
type,cash,price,bonus_ratio
“milk”,12,2,5
“dark”,13,4,1
“white”,6,2,2
```

_Output_: Number of each type of chocolate for that given order
```
milk 7,dark 0,white 0
milk 0,dark 9,white 0
milk 1,dark 0,white 4
```

### Set Up

Place your input csv file into the order_process/lib/input directory. 

* The file should be formatted with the following columns: type, cash, price, and bonus_ratio.
* Please ensure the chocolate name is in double quotes (ex: "milk") and the other values are integers.     
* There is a sample input file for your convenience called 'orders_sample.csv' in the input directory.

### Run Application
  
Navigate to the chocolates_for_bobby/order_processor directory and run the main.py file
```
>> cd chocolates_for_bobby &&  python3 main.py order_processor/lib/input/<filename>.csv 
```

Be sure to replace {your_file_name} with the file you just placed in the input folder. Ex) 
```
>> cd chocolates_for_bobby && python3 main.py order_processor/lib/input/orders_sample.csv 
```

You should see the output in the terminal formatted like so
```
milk 7,dark 0,white 0
milk 0,dark 9,white 0
milk 1,dark 0,white 4
```

### Testing
```
>> python3 -m unittest discover order_processor/tests
```

### Linting
Manual
```
>> pycodestyle --show-source --show-pep8 order_processor/lib/<filename>.py
```
Auto
```
>> autopep8 --in-place --recursive .
```

### Design Notes -
* __Package Management__ - I opted for a context.py rather than a setup.py as per https://docs.python-guide.org/writing/structure/

* __Stateless__ - no need for a DB for now

### Future Work 

Readability
* Consider looking to see if Python has a testing library like rspec with describe, etc blocks instead of long names.
* Give pycodestyle linting instructions for all files (not just 1 at a time).
* Add the linting and testing to a pre-commit hook.
* Consider dockerizing the setup.
* Figure out why autopep8 isn't fixing line length lints - would like the two to agree.
* My tabs and spaces may be mixed - not sure if autopep8 covers that.
* Change order.get_string_output to __str__ (This would be more canonical).

Refactorability
* Consider adding typing to make refactoring easier

Best Practices
* Add standard python gitignore. Noticing pycache specifically but I'm sure there is more.
