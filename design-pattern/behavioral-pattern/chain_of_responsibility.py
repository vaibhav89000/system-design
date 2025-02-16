# 🚀 Chain of Responsibility Example: Authentication Middleware 🔐
# 📌 Scenario
# You are building a web application where each request goes through multiple authentication checks:
# 1️⃣ API Key Check – Ensures the request has a valid API key.
# 2️⃣ User Authentication – Checks if the user is authenticated.
# 3️⃣ Role Authorization – Verifies if the user has the required permissions.

# Each step can either handle the request or pass it to the next step in the chain.

# 🔴 Without Chain of Responsibility (Hardcoded If-Else Mess) 😵

def authenticate_request(request):
    if not request.get("api_key"):
        print("❌ API Key missing!")
        return
    
    if not request.get("user"):
        print("❌ User not authenticated!")
        return

    if request.get("role") != "admin":
        print("❌ Unauthorized! Only admins can access this.")
        return

    print("✅ Request processed successfully!")

# Simulating API request
request = {"api_key": "12345", "user": "JohnDoe", "role": "admin"}
authenticate_request(request)

# 💣 Problems:
# Adding new authentication steps requires modifying the function.
# Tightly coupled logic; not reusable in other parts of the application.

# ✅ With Chain of Responsibility (Flexible & Extensible)
# Step 1: Base Handler (Abstract Class)
class Middleware:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler  # Next handler in the chain

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return True  # If no next handler, request is approved


# Step 2: Concrete Middleware Handlers
class APIKeyMiddleware(Middleware):
    def handle(self, request):
        if not request.get("api_key"):
            print("❌ API Key missing!")
            return False
        print("✅ API Key verified!")
        return super().handle(request)  # Pass to next handler


class AuthMiddleware(Middleware):
    def handle(self, request):
        if not request.get("user"):
            print("❌ User not authenticated!")
            return False
        print("✅ User authenticated!")
        return super().handle(request)


class RoleMiddleware(Middleware):
    def handle(self, request):
        if request.get("role") != "admin":
            print("❌ Unauthorized! Only admins can access this.")
            return False
        print("✅ User authorized!")
        return super().handle(request)


# Step 3: Create the Authentication Chain (API Key → Auth → Role)
auth_chain = APIKeyMiddleware(AuthMiddleware(RoleMiddleware()))

# Step 4: Client Code (Processing Requests)
request1 = {"api_key": "12345", "user": "JohnDoe", "role": "admin"}
request2 = {"api_key": "12345", "user": "JaneDoe", "role": "guest"}

print("\n🔹 **Processing Request 1**")
auth_chain.handle(request1)  # ✅ Success

print("\n🔹 **Processing Request 2**")
auth_chain.handle(request2)  # ❌ Unauthorized

# 🔑 Key Benefits
# ✅ Easily Extensible – You can add new middleware handlers without modifying existing ones.
# ✅ Loose Coupling – Each middleware works independently.
# ✅ Reusable Middleware – The same middleware can be used in different parts of the app.

# 💡 Where is this Used?
# 🔹 Django & Express.js Middleware – Authentication, logging, error handling.
# 🔹 API Gateway Security – Validating API keys, rate limiting, and authorization.
# 🔹 Payment Processing Pipelines – Card validation, fraud detection, balance check.


