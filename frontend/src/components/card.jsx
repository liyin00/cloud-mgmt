import React, { Component } from 'react';
import {Link} from 'react-router-dom';

class Card extends Component {
    state = {}

    formatPrice = () => {
        const price = this.props.product.data.price;
        //Number(price).toFixed(2) will fix the number at 2dp
        return "SGD $" + String(Number(price).toFixed(2));
    }

    // formatValue = () => {
    //     const itemArray = this.props.cart.filter(item=>item.productId == this.props.product.productId);
    //     return itemArray.length == 0 ? 'Add to Cart': itemArray[0].value + ' in Cart';
    // }

    // formatButton = () => {
    //     let buttonClass = 'btn btn-';
    //     let isNum = parseInt(this.formatValue());
    //     isNaN(isNum) ? buttonClass += 'warning' : buttonClass += 'white border';
    //     return buttonClass;
    // }

    formatUrl = () => {
        //adds "-" between words and converts to lowercase
        let url = this.props.product.data.product_name.split(' ').join('-').toLowerCase();
        return encodeURI(url);   
    }

    displayStockCount = () => {
        let count = '';
        if (this.props.product.quantity === 0 ) count = 'Sold Out';
        return count;
    }

    formatStockCount = () => {
        let className = '';
        if (this.props.product.quantity === 0 ) className += 'text-danger';
        return className;
    }

    displayCartItem = () => {
        const itemArray = this.props.cart.filter(item=>item.product_id === this.props.product.product_id);
        return itemArray.length !== 0 ? 'Item added to Cart' : 0;
    }

    render() { 
        const { product, onIncrement, onProductData } = this.props;
        const { product_id } = product
        const { product_name, product_img } = product.data;

        return (
            <div className="card border border-light mx-auto">
                <img className="card-img-top rounded" src={ product_img } alt=""/>
                <div className="card-body">
                    <div className="card-text">
                        <Link to = { `/shop/${product_id}/${this.formatUrl()}` } className="text-dark font-weight-bold" onClick={() => onProductData(product)} >{ product_name }</Link>
                        <br/>
                        <p className='my-2'>{ this.formatPrice() }</p>
                        <p className={ this.formatStockCount() }>{ this.displayStockCount() }</p>
                        { this.displayCartItem() !== 0 && (<Link to="/cart" className='btn border tertiary-bg'>{ this.displayCartItem() }</Link>) }
                        { this.product && <h3>String(this.product)</h3> }
                        
                        {/* <p>{ this.displayCartItem() }</p> */}
                        {/* <button className={ this.formatButton()} onClick={() => onIncrement(product) }>
                            { this.formatValue() }
                        </button> */}
                    </div>
                </div>
            </div>
        );
    }
}

export default Card;