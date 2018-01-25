# legislative-contact

code to pull just contact information for all state legislators from Sunlight Foundation's Open States API.


Notes:

1. the csv here is not up to date, so you should re-run this code locally if you want the current status of the API
1. you will need your own [API key](https://openstates.org/api/register/)
1. to run:
  1. clone repo
  1. (recommended) create a virtual environment
  1. `pip install -r requirements.txt`
  1. create a file called `local_settings.py` and add the line `API_KEY=your-openstates-api-key`
  1. `python get_contacts.py`
