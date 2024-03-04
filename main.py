import os

# Get the value of a specific environment variable
variable_name = "OPENAI_API_KEY"
variable_value = os.getenv(variable_name)
print(f"The value of {variable_name} is: {variable_value}")
