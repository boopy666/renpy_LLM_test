init python:
    import requests

    def test_connection(prompt):
        # Initialize the necessary variables
        url = "http://127.0.0.1:5000/v1/chat/completions"  # Your Oobabooga server URL

        headers = {
            "Content-Type": "application/json",
            "Authorization": "1111",  # Replace with actual token if needed
        }

        data = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt  # Append Fiona's context
                }
            ],
            "mode": "chat",
            "character": "Maddy"
        }

        try:
            response = requests.post(url, headers=headers, json=data, verify=False)
            if response.status_code == 200:
                return {"success": True, "data": response.json()}
            else:
                return {"success": False, "error": "Error from server: {} {}".format(response.status_code, response.text)}
        except Exception as e:
            return {"success": False, "error": "Error sending request: " + str(e)}

    def send_prompt(prompt):
        return test_connection(prompt)
