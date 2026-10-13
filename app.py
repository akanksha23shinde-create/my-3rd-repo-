"""A tiny Python app used to demonstrate a CI/CD pipeline."""

def greet(name: str = "DevOps") -> str:
    """Return a friendly greeting."""
    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "DevOps"
    return f"Hello, {cleaned_name}! Python CI/CD pipeline is working."


if __name__ == "__main__":
    print(greet())
