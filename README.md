<h1>Coffee Shop Challenge <span class="emoji">☕</span></h1>
<p>A Python implementation of a coffee shop domain model with Customer, Coffee, and Order classes demonstrating object-oriented programming principles and many-to-many relationships.</p>
<h2>Project Structure</h2>
<div class="file-structure">
<ul>
  <li>coffee-shop-challenge/</li>
  <li>coffee_shop/  # Package directory</li>
    <ul>
      <li>__init__.py </li>
      <li>coffee.py </li>
      <li>customer.py </li>
      <li>order.py </li>
    </ul>
  <li>tests/  # Test suite</li>
    <ul>
      <li>__init__.py</li>
      <li>coffee_test.py</li>
      <li>customer_test.py</li>
      <li>order_test.py</li>
    </ul>
  <li>setup.py  </li>
  <li>Pipfile </li>
  <li>README.md </li>
</ul>
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
<h3>Order</h3>
    <ul>
        <li><strong>Attributes</strong>:
            <ul>
                <li><code>customer</code> (Customer instance)</li>
                <li><code>coffee</code> (Coffee instance)</li>
                <li><code>price</code> (float, 1.0-10.0, immutable)</li>
            </ul>
        </li>
    </ul>
    
   <h2>Installation</h2>
    
   <ol>
       <li>Clone the repository:
            <pre><code>git clone https://github.com/your-username/coffee-shop-challenge.git
cd coffee-shop-challenge</code></pre>
        </li>
        <li>Set up the environment:
            <pre><code>pipenv install
pipenv install -e .</code></pre>
        </li>
    </ol>
    
   <h2>Running Tests</h2>
    
   <p>Execute all tests:</p>
    <pre><code>pipenv run pytest</code></pre>
    
   <p>Run specific test file:</p>
    <pre><code>pipenv run pytest tests/coffee_test.py -v</code></pre>
    
   <h2>Example Usage</h2>
    
   <pre><code>from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

# Create instances
customer = Customer("Alice")
coffee = Coffee("Latte")

# Create order
order = Order(customer, coffee, 4.5)

# Get customer's orders
print(customer.orders())  # [&lt;Order object&gt;]

# Get coffee's average price
print(coffee.average_price())  # 4.5</code></pre>
    
   <h2>Key Features</h2>
    
   <ul>
        <li>Proper type validation for all attributes</li>
        <li>Immutable properties where specified</li>
        <li>Circular import resolution</li>
        <li>Comprehensive test coverage</li>
        <li>Many-to-many relationships via Order join model</li>
    </ul>
    
   <h2>Dependencies</h2>
    
   <ul>
        <li>Python 3.7+</li>
        <li>pytest (for testing)</li>
        <li>pipenv (for dependency management)</li>
    </ul>
    
   <h2>License</h2>
    
   <p>MIT</p>
