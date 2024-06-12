from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
from auth_bearer import JWTBearer, decodeJWT
import schemas
from commom import get_session, token_required


router = APIRouter(prefix="/products", tags=["Products"])


@router.get('/get_all')
@token_required
async def get_products(dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    products = session.query(models.Product).filter(models.Product.related_user_id == user_id).all()
    return products


@router.get('/get/{product_id}')
@token_required
async def get_product(product_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_product = session.query(models.Product).filter(models.Product.id == product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")
    
    if (existing_product.related_user_id != user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    return existing_product


@router.post('/create')
@token_required
async def create_product(product: schemas.ProductCreate, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    new_product = models.Product(name=product.name, description=product.description, related_user_id=user_id, price=product.price)
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return {"message": "Product created successfully"}


@router.put('/update')
@token_required
async def update_product(product: schemas.ProductUpdate, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_product = session.query(models.Product).filter(models.Product.id == product.id).first()
    if existing_product is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")

    if existing_product.related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    session.commit()
    return {"message": "Product updated successfully"}


@router.patch('/update_partial')
@token_required
async def update_partial_product(product: schemas.ProductFetch, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    existing_product = session.query(models.Product).filter(models.Product.id == product.id).first()
    if existing_product is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")

    if existing_product.related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    if product.name:
        existing_product.name = product.name
    
    if product.description:
        existing_product.description = product.description

    if product.price:
        existing_product.price = product.price

    session.commit()
    return {"message": "Product updated successfully"}


@router.delete('/delete/{product_id}')
@token_required
async def delete_product(product_id: int, dependencies: str = Depends(JWTBearer()), session: Session = Depends(get_session)):
    token = dependencies
    payload = decodeJWT(token)
    user_id = payload['sub']

    query_result = session.query(models.Product).filter(models.Product.id == product_id)
    if query_result.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product not found")

    if query_result.first().related_user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    query_result.delete()
    session.commit()

    return {"message": "Product deleted successfully"}