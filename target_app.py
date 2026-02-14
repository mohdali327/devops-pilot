def process_user_data(data):
    # Check if 'email' exists in the dictionary before trying to access it
    if 'email' in data and 'name' in data:
        print(f"Processing user: {data['name']} with email {data['email']}")
    else:
        print("Error: Missing 'email' or 'name' key in the dictionary.")

if __name__ == "__main__":
    sample_user = {"name": "Mohd Ali"}
    process_user_data(sample_user)