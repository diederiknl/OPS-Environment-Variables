import os

# Get the value of a specific environment variable
variable_name = "USER"
variable_value = os.getenv(variable_name)
print(f"The value of {variable_name} is: {variable_value}")

# Print all environment variables
print("All environment variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")