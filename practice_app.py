from fastapi import FastAPI
app =  FastAPI(debug=True)
#from orders.api impor api

from uuid import UUID
from fastapi.openapi.models import Response
from starlette import status
from orders.app import app
order = { #A
'id': 'ff0f1355-e821-4178-9567-550dec27a373',
'status': 'completed',
'created': 1740493805,
'order': [
{
'product': 'cappuccino',
'size': 'medium',
'quantity': 1
}
]
}
@app.get('/orders') #B
def get_orders():
return [
order
]