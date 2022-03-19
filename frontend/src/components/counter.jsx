import React, { Component } from 'react';

class Counter extends Component {
    state = {}

    formatValue(){
        const itemArray = this.props.cart.filter(item=>item.productId == this.props.productId);
        return itemArray.length == 0 ? 'Add to Cart': itemArray[0].value;
    }

    render() {
        const {productId, onIncrement} = this.props;

        return (
            <button className="btn btn-secondary" 
            onClick={() => onIncrement(productId)}>{this.formatValue()}</button>
        );
    }
}

export default Counter;

