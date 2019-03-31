from cloudant_service import CloudantService

connection_credentials = {'user': None,
                          'auth_token': None,
                          'url': 'https://mikerhodes.cloudant.com',
                          'admin_party': True,
                          'connect': True
                          }
db_name = 'airportdb'
cloudant = CloudantService(**connection_credentials)
dd = cloudant.get_airport_data(lat_dn=0, lon_dn=0, lon_up=30, lat_up=5)
print(dd)
