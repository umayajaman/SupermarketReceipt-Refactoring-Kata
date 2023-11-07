# Scope for improvements
1. Add documentation for all the class methods
2. Associate unit price with the `Product` class. Then, it is not necessary to pass the whole catalog to the [`Teller`](https://github.com/umayajaman/SupermarketReceipt-Refactoring-Kata/blob/main/python/teller.py#L11)
   ```python
   class Product:
       def __init__(self, name: str, unit: "ProductUnit", 
                    price: float):
           self.name = name
           self.unit = unit
           self.price = price
    ```
3. Split the [`handle_offers`](https://github.com/umayajaman/SupermarketReceipt-Refactoring-Kata/blob/main/python/shopping_cart.py#L36) method
4. Write a `print_()` method in the `Receipt` class. This eliminates the need of separate class to print it 
5. Follow dependency injection pattern to make the code more readable and testable.
   e.g. Pass `ReceiptItem` to `Receipt.add_product()` instead of creating one inside the [class method](https://github.com/umayajaman/SupermarketReceipt-Refactoring-Kata/blob/main/python/receipt.py#L37)
6. Make the code more pythonic
   * Get dictionary key-value pair using `dict.items()`. e.g. [handle_offers](https://github.com/umayajaman/SupermarketReceipt-Refactoring-Kata/blob/main/python/shopping_cart.py#L40)
   * Use format strings instead of complex string manipulation. e.g. [ReceiptPrinter](https://github.com/umayajaman/SupermarketReceipt-Refactoring-Kata/blob/main/python/receipt_printer.py#L9)
