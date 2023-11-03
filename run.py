import requests
from rich import print as rprint
import emoji

# Make a GET request
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    rprint(f"[green]Title of the todo: {data['title']}[/green]")
    rprint(emoji.emojize(":check_mark_button: Success! :beaming_face_with_smiling_eyes:"))
else:
    rprint(f"Request failed with status code {response.status_code}")
    rprint(emoji.emojize(":cross_mark: Failure!"))