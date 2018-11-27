from __future__ import print_statement
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
# Integer | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
before = 56
# Integer | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
after = 56
page = 56  # Integer | Page number. (optional)
perPage = 56  # Integer | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Activities
    api_response = api_instance.getLoggedInAthleteActivities(before=before, after=after, page=page, perPage=perPage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getLoggedInAthleteActivities: %s\n" % e)
