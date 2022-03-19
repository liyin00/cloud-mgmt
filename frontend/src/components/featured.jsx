import React, { Component } from 'react';
import Carousel from './carousel';
import {Link} from 'react-router-dom';

class Featured extends Component {
    state = {}
    render() {
        const {cart, onIncrement, products} = this.props;

        return (
            <div className="container mt-5 mx-auto">
                <Link to="/shop/dog-collection" className="collection">
                    <p>Doggo Special Collection.</p>
                </Link>
                <Carousel products={products} cart={cart} onIncrement={onIncrement} />
            </div>
        );
    }
}

export default Featured;