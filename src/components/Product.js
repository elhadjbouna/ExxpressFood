import React from 'react'
import { Card } from 'react-bootstrap'
import Rating from './Rating'
import { Link } from 'react-router-dom'

function Product({ product }) {
    return (
        <Card className="my-3 p-3 rounded">
            <Link to={`/product/${product.PlatId}`}>
                <Card.Img src={product.image} />
            </Link>

            <Card.Body>
                <Link to={`/product/${product.PlatId}`}>
                    <Card.Title as="div">
                        <strong>{product.PlatName}</strong>
                    </Card.Title>
                </Link>

               {product.PlatName &&

               <Card.Text as="div">
                    <div className="my-3">
                        <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                    </div>
                </Card.Text>
               }
                


               {product.price &&
                <Card.Text as="h3">
                    ${product.price}
                </Card.Text>
               } 
            </Card.Body>
        </Card>
    )
}

export default Product
