import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import BreadCrumb from './breadcrumb';
import Alert from './alert';

class Product extends Component {
    state = {
        product : [],
        alert: false
    }

    componentDidMount() {
        if (this.props.product.length === 0) {
            //call of product using productId
            let product = {productId: 2, productName: "Dog Tag", productPrice: 9.9, description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 10, imgSrc: './images/dog_tags2.jpg'};
            this.setState({ product: product });
        }
        else {
            this.setState({product: this.props.product});
        }

    }

    formatPrice = () => {
        let price = this.state.product.productPrice;
        return "SGD $" + String(Number(price).toFixed(2));
    }

    // Formats and displays add to cart button
    formatValue = () => {
        const itemArray = this.props.cart.filter(item=>item.productId === this.props.product.productId);
        return itemArray.length === 0 ? 'Add to Cart': itemArray[0].value + ' in Cart';
    }

    formatButton = () => {
        let buttonClass = 'add-to-cart-btn btn primary-bg';
        let isNum = parseInt(this.formatValue());
        // isNaN(isNum) ? buttonClass += 'text-white primary-bg' : buttonClass += 'text-dark primary-bg';
        return buttonClass;
    }

    //Formats and displays stock availability indicator
    displayStockCount = () => {
        let count = (this.state.product.stockCount === 0) ? 'Sold Out' : 'In Stock';
        return count;
    }

    formatStockCount = () => {
        let className = 'mx-4 ';
        this.state.product.stockCount === 0 ? className += 'text-danger' : className += 'text-success';
        return className;
    }

    onAddToCart = () => {
        this.setState({ alert: true });

    }

    handleCloseAlert = () => {
        this.setState({ alert: false });
    }
    
    render() {
        const {onIncrement, cart} = this.props;
        const {productName, imgSrc, description} = this.state.product;

        return (
            // <h1>{`The productId is: ${this.props.match.params.productId}`}</h1>
            <div>
                <BreadCrumb productName={ productName } />
                <div className="row">
                    <div className="col-sm-7 product container">
                        <div className="d-block text-center">
                            {/* <div className="product-img-center"> */}
                            <div>
                                <img className="product-img" src={ imgSrc } alt="" />
                            </div>
                        </div>
                        <div className="d-block mt-4 d-flex justify-content-center">
                            <div className="product-gallery">
                                <img className="product-gallery-img" src={ imgSrc } alt="" />
                                <img className="product-gallery-img" src={ imgSrc } alt="" />
                                <img className="product-gallery-img" src={ imgSrc } alt="" />
                            </div>
                        </div>
                    </div>
                    <div className="col-sm-5 product-info-container">
                        <div className="product-info">
                            <h3>{ productName }</h3>
                            <div className="py-3 d-flex justify-content-between">
                                <span className="mx-4 font-weight-bold">{ this.formatPrice() }</span>
                                <span className={ this.formatStockCount() }><u>{ this.displayStockCount() }</u></span>
                            </div>
                            <p>{ description }</p>
                            <button 
                                className={ this.formatButton() } 
                                onClick={() => {onIncrement(this.state.product); this.onAddToCart();}}
                                //prevent adding to cart if a product is out of stock
                                disabled={ this.state.product.stockCount === 0 ? true : false }>
                                {/* { this.formatValue() } */}
                                Add to Cart
                            </button>
                        </div>
                    </div>
                    <div className="col-sm-12 d-flex justify-content-center">
                        { this.state.alert && <Alert cart={cart} product={this.state.product} onCloseAlert={this.handleCloseAlert} /> }
                    </div>
                </div>

            </div>
        );
    }
}

export default withRouter(Product);
// solved by adding