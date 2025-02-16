# Proxy Design Pattern 🕵️‍♂️
# The Proxy Pattern is a structural design pattern that acts as a substitute or intermediary for another object. It controls access to the real object, adding security, caching, or lazy initialization.

# 📌 When to Use the Proxy Pattern?
# ✅ When direct access to an object is expensive or restricted.
# ✅ When you need lazy initialization (object creation only when needed).
# ✅ When you want to add security, logging, caching, or access control before interacting with the real object.

# 🚀 Real-World Example: Internet Access Proxy
# Imagine a company that restricts internet access for employees. Instead of directly accessing the internet, requests go through a proxy server, which filters allowed and blocked websites.

# 🔴 Without Proxy (Direct Access)
class Internet:
    def connect(self, website):
        print(f"Connecting to {website}")

# Direct access to the internet
internet = Internet()
internet.connect("google.com")
internet.connect("facebook.com")  # ❌ Should be blocked

# 🚨 Problem:
# No control over website access.
# Employees can access restricted websites.


# ✅ With Proxy (Controlled Access)
# Step 1: Define the Subject (Real Internet Access)
class Internet:
    def connect(self, website):
        print(f"Connecting to {website}")

# Step 2: Proxy Class (Controls Access)
class ProxyInternet:
    blocked_sites = {"facebook.com", "instagram.com", "youtube.com"}  # Restricted sites

    def __init__(self):
        self.real_internet = Internet()

    def connect(self, website):
        if website in self.blocked_sites:
            print(f"Access to {website} is BLOCKED ❌")
        else:
            self.real_internet.connect(website)  # Forward request

# Step 3: Client Code
internet = ProxyInternet()
internet.connect("google.com")  # ✅ Allowed
internet.connect("facebook.com")  # ❌ Blocked
internet.connect("stackoverflow.com")  # ✅ Allowed

# 🔹 How Does It Work?
# ✅ ProxyInternet acts as a middleman, checking access rules before forwarding requests.
# ✅ If the website is blocked, it denies access.
# ✅ If allowed, it forwards the request to the real Internet object.

# 🔑 Key Benefits of the Proxy Pattern
# ✔️ Controls access – Restricts or filters interactions with the real object.
# ✔️ Lazy initialization – Delays object creation until it's actually needed.
# ✔️ Enhances security – Blocks unauthorized access.
# ✔️ Improves performance – Can cache results to reduce expensive operations.
# ✔️ Adds logging and monitoring – Tracks object interactions.

# 🚀 Real-World Use Cases
# Virtual Proxy – Loading large images only when displayed.
# Security Proxy – Restricting access to sensitive data.
# Cache Proxy – Storing API responses to reduce redundant calls.
# Remote Proxy – Controlling access to remote objects (e.g., database connection).
# Smart References – Keeping track of object references to manage resources efficiently.
