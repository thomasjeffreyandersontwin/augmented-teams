# Mamba/Python BDD Behavior Reference

This document provides comprehensive examples for `bdd-mamba-rule.mdc`.

See `bdd-rule.mdc` for core BDD principles.

## Table of Contents
1. [Business Readable Language](#1-business-readable-language)
2. [Comprehensive and Brief](#2-comprehensive-and-brief)
3. [Balance Context Sharing](#3-balance-context-sharing)
4. [Cover All Layers](#4-cover-all-layers)
5. [Front-End Testing](#5-front-end-testing)

---

## 1. Business Readable Language

### 1.1 Fluent Subject-Focused Descriptions

**Good Examples:**

```python
from mamba import description, context, it

# Example 1: User authentication
with description('a user that is being authenticated') as self:
    with context('with valid credentials'):
        with it('should receive an access token'):
            pass
    
    with context('with expired credentials'):
        with it('should receive an expiration error'):
            pass

# Example 2: Order processing
with description('an order that is being processed') as self:
    with context('with valid payment'):
        with it('should transition to confirmed status'):
            pass
    
    with context('with insufficient funds'):
        with it('should transition to payment failed status'):
            pass

# Example 3: Document upload
with description('a document that is being uploaded') as self:
    with context('that meets size requirements'):
        with it('should be stored in the repository'):
            pass
    
    with context('that exceeds size limits'):
        with it('should be rejected with size error'):
            pass
```

**Bad Examples:**

```python
# Missing subject - too generic
with description('authentication'):  # Who is being authenticated?
    with it('should work'):
        pass

# Action verb in describe
with description('when authenticating users'):  # Use nouns, not verbs
    pass

# Skipped concepts
with description('validation'):  # What is being validated? Under what conditions?
    pass
```

### 1.2 Natural Sentence Flow

Tests should read naturally when combined:

```python
# Reads: "A shopping cart that has items should calculate total price"
with description('a shopping cart') as self:
    with context('that has items'):
        with it('should calculate total price'):
            pass

# Reads: "A shopping cart that is empty should show zero total"
with description('a shopping cart') as self:
    with context('that is empty'):
        with it('should show zero total'):
            pass
```

---

## 2. Comprehensive and Brief

### 2.1 Cover All Paths

**Good Example - Comprehensive Coverage:**

```python
with description('a user registration service') as self:
    with context('registration with valid data'):
        with it('should create user account'):
            pass
        
        with it('should send welcome email'):
            pass
    
    with context('registration with duplicate email'):
        with it('should raise DuplicateEmailError'):
            pass
    
    with context('registration with invalid email format'):
        with it('should raise ValidationError'):
            pass
    
    with context('registration with weak password'):
        with it('should raise WeakPasswordError'):
            pass
    
    with context('registration when email service is unavailable'):
        with it('should create account but log email failure'):
            pass
```

### 2.2 Keep Tests Brief

```python
# Good - brief and focused
with it('should calculate discount'):
    order = Order(total=100)
    order.apply_discount(10)
    expect(order.discounted_total).to(equal(90))

# Bad - too long
with it('should process order'):
    # 50 lines of setup and assertions
    # Testing too many things at once
    pass
```

---

## 3. Balance Context Sharing

### 3.1 Use before.each for Shared Setup

**Good Example:**

```python
from mamba import description, context, it, before
from expects import expect, equal

with description('a product service') as self:
    with before.each:
        # Shared setup
        self.repository = FakeProductRepository()
        self.service = ProductService(self.repository)
        
        # Helper factory
        def create_product(**overrides):
            defaults = {
                'name': 'Widget',
                'price': 10.00,
                'in_stock': True
            }
            defaults.update(overrides)
            return Product(**defaults)
        
        self.create_product = create_product
    
    with context('finding a product by ID'):
        with context('that exists'):
            with it('should return the product'):
                product = self.create_product(id='prod-123')
                self.repository.save(product)
                
                result = self.service.find_by_id('prod-123')
                
                expect(result).to(equal(product))
        
        with context('that does not exist'):
            with it('should return None'):
                result = self.service.find_by_id('nonexistent')
                expect(result).to(be(None))
```

### 3.2 Avoid Duplication

**Bad Example:**

```python
# Duplicating setup in every test
with it('test 1'):
    service = ProductService()
    repo = FakeRepository()
    product = Product(name='Widget', price=10.00)
    # ...

with it('test 2'):
    service = ProductService()
    repo = FakeRepository()
    product = Product(name='Widget', price=10.00)
    # ...
```

---

## 4. Cover All Layers

### 4.1 Service Layer (Business Logic)

```python
from mamba import description, context, it, before
from doublex import Spy, when

with description('a payment service') as self:
    with before.each:
        self.payment_gateway = Spy(PaymentGateway)
        self.notification_service = Spy(NotificationService)
        self.service = PaymentService(
            payment_gateway=self.payment_gateway,
            notification_service=self.notification_service
        )
    
    with context('processing a payment'):
        with context('that succeeds'):
            with it('should charge the payment gateway'):
                when(self.payment_gateway).charge(100.00).returns(True)
                
                result = self.service.process_payment(amount=100.00)
                
                expect(result.success).to(be_true)
                expect(self.payment_gateway.charge).to(have_been_called_with(100.00))
            
            with it('should send success notification'):
                when(self.payment_gateway).charge(100.00).returns(True)
                
                self.service.process_payment(amount=100.00)
                
                expect(self.notification_service.send_success).to(have_been_called)
        
        with context('that fails'):
            with it('should not send success notification'):
                when(self.payment_gateway).charge(100.00).returns(False)
                
                self.service.process_payment(amount=100.00)
                
                expect(self.notification_service.send_success).not_to(have_been_called)
```

### 4.2 Repository Layer (Data Access)

```python
with description('a user repository') as self:
    with before.each:
        self.db = InMemoryDatabase()
        self.repository = UserRepository(self.db)
    
    with context('saving a user'):
        with it('should persist to database'):
            user = User(id='user-123', email='alice@example.com')
            
            self.repository.save(user)
            
            saved = self.db.find('users', 'user-123')
            expect(saved['email']).to(equal('alice@example.com'))
    
    with context('finding a user by email'):
        with context('that exists'):
            with it('should return the user'):
                user = User(id='user-123', email='alice@example.com')
                self.repository.save(user)
                
                result = self.repository.find_by_email('alice@example.com')
                
                expect(result.id).to(equal('user-123'))
```

---

## 5. Front-End Testing

### 5.1 UI Component Behavior

For Python web frameworks (Flask, Django, FastAPI):

```python
from mamba import description, context, it, before
from flask import Flask
from flask.testing import FlaskClient

with description('a user profile page') as self:
    with before.each:
        self.app = create_app({'TESTING': True})
        self.client = self.app.test_client()
        self.user_service = FakeUserService()
    
    with context('for an authenticated user'):
        with context('with complete profile'):
            with it('should display user name'):
                self.user_service.set_current_user(
                    User(name='Alice Smith', email='alice@example.com')
                )
                
                response = self.client.get('/profile')
                
                expect(response.data).to(contain(b'Alice Smith'))
        
        with context('with incomplete profile'):
            with it('should show completion prompt'):
                self.user_service.set_current_user(
                    User(name=None, email='alice@example.com')
                )
                
                response = self.client.get('/profile')
                
                expect(response.data).to(contain(b'Complete your profile'))
    
    with context('for an unauthenticated user'):
        with it('should redirect to login'):
            response = self.client.get('/profile')
            
            expect(response.status_code).to(equal(302))
            expect(response.location).to(contain('/login'))
```

---

## Common Patterns

### Factory Pattern

```python
def create_user(**overrides):
    """Create test user with defaults that can be overridden."""
    defaults = {
        'id': 'user-123',
        'email': 'test@example.com',
        'name': 'Test User',
        'active': True,
        'created_at': datetime.now()
    }
    defaults.update(overrides)
    return User(**defaults)

# Usage
user = create_user(email='alice@example.com', active=False)
```

### Spy/Stub Pattern with Doublex

```python
from doublex import Spy, when, ANY_ARG

# Create spy
email_service = Spy(EmailService)

# Stub return value
when(email_service).send_email(ANY_ARG).returns(True)

# Verify call
expect(email_service.send_email).to(have_been_called_with(
    to='alice@example.com',
    subject='Welcome'
))
```

### Async Testing

```python
import asyncio
from mamba import description, it

with description('an async service') as self:
    with it('should fetch data asynchronously'):
        async def test():
            service = AsyncDataService()
            result = await service.fetch_data('user-123')
            expect(result).not_to(be(None))
        
        asyncio.run(test())
```

---

## Edge Cases and Gotchas

### 1. Testing Exceptions

```python
from expects import raise_error

with it('should raise ValidationError for invalid input'):
    service = ValidationService()
    
    def validate_invalid():
        service.validate({'email': 'not-an-email'})
    
    expect(validate_invalid).to(raise_error(ValidationError))
    expect(validate_invalid).to(raise_error(ValidationError, 'Invalid email format'))
```

### 2. Testing None/Empty Values

```python
with it('should handle None gracefully'):
    service = UserService()
    
    result = service.find_by_id(None)
    
    expect(result).to(be(None))

with it('should handle empty string'):
    service = UserService()
    
    result = service.find_by_email('')
    
    expect(result).to(be(None))
```

### 3. Testing Collections

```python
from expects import have_length, contain, be_empty

with it('should return multiple results'):
    service = ProductService()
    
    results = service.search('widget')
    
    expect(results).to(have_length(3))
    expect(results).to(contain(product1))

with it('should return empty list when no matches'):
    service = ProductService()
    
    results = service.search('nonexistent')
    
    expect(results).to(be_empty)
```

---

This reference provides comprehensive examples for all BDD principles in Mamba/Python context. For core principles, always refer to `bdd-rule.mdc`. For quick patterns, see `bdd-mamba-rule.mdc`.

