<h1>Coffee Shop Challenge <span class="emoji">☕</span></h1>
<p>A Python implementation of a coffee shop domain model with Customer, Coffee, and Order classes demonstrating object-oriented programming principles and many-to-many relationships.</p>
<h2>Project Structure</h2>
<div class="file-structure">
coffee-shop-challenge/
├── coffee_shop/               # Package directory
│   ├── __init__.py            # Package initialization
│   ├── coffee.py              # Coffee model
│   ├── customer.py            # Customer model
│   ├── order.py               # Order model
├── tests/                     # Test suite
│   ├── __init__.py
│   ├── coffee_test.py
│   ├── customer_test.py
│   └── order_test.py
├── setup.py                   # Package configuration
├── Pipfile                    # Dependencies
└── README.md                  # This file
    </div>
    
  <h2>Models</h2>
    
  <h3>Customer</h3>
    <ul>
        <li><strong>Attributes</strong>:
            <ul>
                <li><code>name</code> (string, 1-15 characters)</li>
            </ul>
        </li>
        <li><strong>Methods</strong>:
            <ul>
                <li><code>orders()</code>: Returns all orders by this customer</li>
                <li><code>coffees()</code>: Returns unique list of coffees ordered</li>
                <li><code>create_order(coffee, price)</code>: Creates new order</li>
            </ul>
        </li>
    </ul>
    
  <h3>Coffee</h3>
    <ul>
        <li><strong>Attributes</strong>:
            <ul>
                <li><code>name</code> (string, ≥3 characters, immutable)</li>
            </ul>
        </li>
        <li><strong>Methods</strong>:
            <ul>
                <li><code>orders()</code>: Returns all orders for this coffee</li>
                <li><code>customers()</code>: Returns unique list of customers who ordered it</li>
                <li><code>num_orders()</code>: Returns total order count</li>
                <li><code>average_price()</code>: Returns mean order price</li>
            </ul>
        </li>
    </ul>
