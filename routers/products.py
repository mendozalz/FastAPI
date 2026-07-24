from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["productos"])

products_list = [
    {"id": 1, "name": "Laptop Gamer", "price": 1299.99, "category": "Tecnología"},
    {"id": 2, "name": "Smartphone X", "price": 799.50, "category": "Tecnología"},
    {"id": 3, "name": "Auriculares Bluetooth", "price": 149.99, "category": "Audio"},
    {"id": 4, "name": "Reloj Inteligente", "price": 219.90, "category": "Deportes"},
    {"id": 5, "name": "Cámara DSLR", "price": 899.00, "category": "Fotografía"},
    {"id": 6, "name": "Teclado Mecánico", "price": 129.99, "category": "Periféricos"},
    {"id": 7, "name": "Mouse Inalámbrico", "price": 59.99, "category": "Periféricos"},
    {"id": 8, "name": "Monitor 4K", "price": 399.99, "category": "Tecnología"},
    {"id": 9, "name": "Altavoz Portátil", "price": 89.90, "category": "Audio"},
    {"id": 10, "name": "Tablet Pro", "price": 649.50, "category": "Tecnología"},
]

@router.get("/")
async def products():
    return products_list