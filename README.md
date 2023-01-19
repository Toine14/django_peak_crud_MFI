# Test project for MFI
This API is coded using Django/ Django rest framework/ GEOdjango/
The database is PostgreSQL with PostGIS extension
This project use the development server provided by Django which is not suitable for production. For production use docker NGINX image and use gunicorn on web image.

## Installation

Require docker and docker compose.

Clone this repo.

Install and everything by doing:
```sh
docker compose up
```

## Use

The API run on **localhost:8000/api/peak**
All coordinates must be in **WGS84** (EPSG 4326)

In order to get all peaks :
`GET localhost:8000/api/peak`

To get a particular peak :
`GET localhost:8000/api/peak/<id>`

To update a particular peak :
`PUT localhost:8000/api/peak/<id>`

To delete a particular peak :
`DELETE localhost:8000/api/peak/<id>`

You can use the embedded doc to POST peak at :
`POST localhost:8000/api/peak`
the location field in the form should be like:
```json
{"type": "Point", "coordinates": [6.952242, 48.1696017]}
```


Or :
`POST localhost:8000/api/peak`
with this content in request body:
```json
{
    "name":"peak_name",
    "elevation":4808,
    "location": {
            "type": "Point",
            "coordinates": [
                6.952242,
                48.1696017 
            ]
        }
}
```

To GET all peaks inside a bounding box use:
`POST localhost:8000/api/peak/bounding_box`
with this content in request body to define the bbox coordinates:
```json
{
    "min_x":-5.679688,
    "min_y":-70.313043,
    "max_x":-18.820313,
    "max_y":-16.553726
}
```
You can also pass bbox coordinates as URL parameters:
`POST localhost:8000/api/peak/bounding_box?min_x=10&min_y=10&max_x=12&max_y=15`
