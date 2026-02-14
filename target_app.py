# target_app.py
def process_user_data(data):
    # This will crash because 'email' is missing in the dictionary
    print(f"Processing user: {data['name']} with email {data['email']}")

if __name__ == "__main__":
    sample_user = {"name": "Mohd Ali"}
    process_user_data(sample_user)