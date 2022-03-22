import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import BreadCrumb from './breadcrumb';
import Alert from './alert';
import {productURL,getProductById} from  '../callAPI/productAPI'
// import {cartURL,createCartItem} from  '../callAPI/cartAPI'


class Product extends Component {
    state = {
        product : [],
        alert: false,
        cart: []
    }

    componentDidMount() {
        if (this.props.product.length === 0) {
            const product_id = window.location.pathname.split("/")[2];
            getProductById(productURL, product_id).then(result => {
                console.log("result is ", result)
                if (result.code == 200) {
    
                    console.log('result is')
                    console.log(result.data)
                    this.error = false;
                    //const courses = result.data;
    
                    this.setState(
                        {   result:result.data,
                            product_id: result.product_id
                        }
                    )
                    
                    //sort courses according to course id in ascending order
                    
                } else {
                    console.log("test")
                    this.error = true;
                }
            });
        } else {
            this.setState({
                result: this.props.product.data,
                product_id: this.props.product.product_id
            });
        }

    }

    formatPrice = () => {
        
        let price = this.state.result.price;
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

    productInCart = (product_id) => {
        const product = this.props.cart.filter(product => product.product_id === product_id)[0];
        console.log("product", product);
        return product ? true: false
    }

    onAlert = () => {
        this.setState({ alert: true });
    }

    // onAddToCart = (test) => {
    //     //user need update HARDCODE
    //     let data = {
    //         'user_id' : 'u6',
    //         'product_id' :  this.state.product_id,
    //         'product_name': this.state.result.product_name,
    //         'product_description': this.state.result.product_description,
    //         'product_img': this.state.result.product_img,
    //         'quantity':'1',
    //         'price' : this.state.result.price

    //     }

    //     // post 

    //     console.log("DATA IS BELOW")
    //     console.log(this.state)
    //     console.log("test")
    //     console.log("data is is is")
    //     console.log(data)
    //     console.log("===========")

    //     //post

    //     createCartItem(cartURL,data).then(result => {
    //         console.log("result is ", result)
    //         if (result.code == 200) {
    //             this.setState({ alert: true });
    //             this.error = false;
    //             //const courses = result.data;
                
                
    //             //sort courses according to course id in ascending order
                
    //         } else {
    //             console.log("test")
    //             this.error = true;
    //         }
    //     });


    //     //this.setState({ alert: true });

    // }

    handleCloseAlert = () => {
        this.setState({ alert: false });
    }
    
    render() {

        if(this.state.result == undefined ){
            console.log("herehehrehrhehreh nothing")
            return null
        }else{
            console.log("value below")
            console.log(this.state.result)
            console.log(this.state.result.product_description)
            // console.log(this.state.result)


            const {onIncrement, cart} = this.props;
            console.log(cart)
            const product_id = this.state.product_id;
            const {product_name, product_img, product_description} = this.state.result;

            return (
                // <h1>{`The productId is: ${this.props.match.params.productId}`}</h1>
                <div>
                    <BreadCrumb productName={ product_name } />
                    <div className="row">
                        <div className="col-sm-7 product container">
                            <div className="d-block text-center">
                                {/* <div className="product-img-center"> */}
                                <div>
                                    <img className="product-img" src={ product_img } alt="" />
                                </div>
                            </div>
                            <div className="d-block mt-4 d-flex justify-content-center">
                                <div className="product-gallery">
                                    <img className="product-gallery-img" src={ product_img } alt="" />
                                    <img className="product-gallery-img" src={ product_img } alt="" />
                                    <img className="product-gallery-img" src={ product_img } alt="" />
                                </div>
                            </div>
                        </div>
                        <div className="col-sm-5 product-info-container">
                            <div className="product-info">
                                <h3>{ product_name }</h3>
                                <div className="py-3 d-flex justify-content-between">
                                    <span className="mx-4 font-weight-bold">{ this.formatPrice() }</span>
                                    <span className={ this.formatStockCount() }><u>{ this.displayStockCount() }</u></span>
                                </div>
                                <p>{ product_description }</p>
                                <button 
                                    className={ this.formatButton() } 
                                    onClick={() => {onIncrement(this.state.result, product_id); this.onAlert()}}
                                    //prevent adding to cart if a product is out of stock
                                    // disabled={ this.state.product.stockCount === 0 ? true : false }>
                                    disabled={ this.productInCart(product_id) }>
                                    {/* { this.formatValue() } */}
                                    Add to Cart
                                </button>
                            </div>

                            <div className="d-flex justify-content-center">
                            { this.state.alert && <Alert product_name={product_name} onCloseAlert={this.handleCloseAlert} /> }
                            </div>
                        </div>
                        {/* <div className="col-sm-5 d-flex justify-content-center">
                            { this.state.alert && <Alert cart={cart} product={this.state.product} onCloseAlert={this.handleCloseAlert} /> }
                        </div> */}
                    </div>

                </div>
            );
        }
    }
}

export default withRouter(Product);
// solved by adding