import React from 'react';

// function displayCartItem() {
//     const itemArray = this.props.cart.filter(item=>item.productId == this.props.product.productId);
//     return itemArray[0].value;
// }

const Alert = ({cart, product, onCloseAlert}) => {
    return (
        <div className="alert alert-success" role="alert">
            You added { cart.filter(item => (item.productId === product.productId))[0].value }
            <strong> { product.productName }</strong> to your cart.
            <button type="button" className="close" onClick={() => onCloseAlert() } >
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    );
}

export default Alert;