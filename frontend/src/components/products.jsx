import React from 'react';
import Card from './card';

const Products = ({products, cart, onIncrement, onProductData}) => {
    return (
        <div className="row">
            {products.map(product =>(
                <div className="col-4 col-xs-6 mb-5" key={product.productId}>
                    <Card product={product} cart={cart} onIncrement={onIncrement} onProductData={onProductData}/>
                </div>
            ))}
        </div>
    );
}

export default Products;