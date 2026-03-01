def process_user_data(data):
    if 'email' in data:
        print(f"Processing user: {data['name']} with email {data['email']}")
    else:
        print(f"Processing user: {data['name']} (no email provided)")

if __name__ == "__main__":
    sample_user = {"name": "Mohd Ali"}
    process_user_data(sample_user)