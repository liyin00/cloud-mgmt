import React, { Component, Suspense } from 'react';
import ScrollToTop from './components/scrollToTop'; //helps to reset scroll during page change
import Navbar from './components/navbar';
import Footer from './components/footer';
import Home from './components/home';
import Shop from './components/shop';
import Product from './components/product';
import Cart from './components/cart';
import './App.css';
import { BrowserRouter as Router, Route, Switch, withRouter  } from 'react-router-dom';

import {productURL, getAllProducts} from './callAPI/productAPI';
import {cartURL, createCartItem, getCartByUserId, modifyCart} from  './callAPI/cartAPI'

class App extends Component {
    state = {
        //retrieve cart items for sessionStorage
        //update state if cart item exists in sessionStorage
        user_id: "",
        cart: [],
        products: [],
        product: []
    };

    componentDidMount() {
        const session = JSON.parse(sessionStorage.getItem("session"));
        if (session) {
            const user_id = session.user_id;
            this.setState({user_id: user_id});

            //get cart data
            if (this.state.cart.length === 0){
                getCartByUserId(cartURL, user_id).then(result => {
                    if (result.code === 200){
                        const response = result.data
                        if (response){
                            this.state.cart = response.product_list;
                            this.state.user_id = response.user_id
                            this.setState(this.state);
                        }
                    } else {
                        console.log("error in getting cart items from home page", result.data);
                    }
                })
            };

        } else {
            window.location.href = "/login.html";
        }
        
    }

    handleIncrement = (product, product_id) => {
        if (this.state.user_id === "") window.location.href = '/login.html';
        else{
            const product_data = {
                'user_id' : this.state.user_id,
                'product_id' :  product_id,
                'product_name': product.product_name,
                'product_description': product.product_description,
                'product_img': product.product_img,
                'quantity':'1',
                'price' : product.price,
                'price_id': product.price_id
            }
    
            const itemArray = this.state.cart.filter(item=>item.product_id == product_data.product_id);
            //create the value attribute in product
            if (itemArray.length === 0) {
                createCartItem(cartURL, product_data).then(result => {
                    console.log("result is ", result)
                    if (result.code === 200) {
                        this.setState({ alert: true });
                        this.error = false;
        
                        const cart = [...this.state.cart];
                        const itemArray = this.state.cart.filter(item=>item.product_id == product_data.product_id);
                        //create the value attribute in product
                        if (itemArray.length === 0) {
                            // convert quantity to numeric to count
                            product_data.quantity = Number(product_data.quantity)
                            cart.push(product_data);
                            this.setState({cart});
                        }
                        
                    } else {
                        console.log("test")
                        this.error = true;
                    }
                    
                })
            }
        }

    }

    onModifyCart = (body, cart) => {
        modifyCart(cartURL, body).then(result => {
            console.log(result)
            if (result.code === 200){
                this.error = false;
                const response = result.data;
                console.log(response);
                this.setState({cart});
            } else {
                console.log("Error in deleting product from cart", result.data);
                this.error = true;
            }
        });
    }


    handleDelete = (product) => {
        const cart = [...this.state.cart];
        const product_data = cart.filter(item => item.product_id === product.product_id)[0];
        const index = cart.indexOf(product_data);
        // cart[index] = {...product};
        cart.splice(index, 1);
        const body = {
            result: {
                "product_list": cart,
                "user_id": this.state.user_id
            }
        }
        this.onModifyCart(body, cart);
    }

    handleChange = (product, selectedQuantity) => {
        const cart = [...this.state.cart];
        const product_data = cart.filter(item => item.product_id === product.product_id)[0];
        const index = cart.indexOf(product_data);
        // cart[index] = {...product};
        cart[index].quantity = String(selectedQuantity);
        const body = {
            result: {
                "product_list": cart,
                "user_id": this.state.user_id
            }
        }
        this.onModifyCart(body, cart);
    }

    handleClearCart = () => {
        const cart = []
        const body = {
            result: {
                "product_list": cart,
                "user_id": this.state.user_id
            }
        }
        this.onModifyCart(body, cart);
    }

    handleTotalCartItems = () => {
        //calculate the sum of items
        return this.state.cart.map(item => Number(item.quantity)).reduce((a,b) => a + b, 0)
    };

    handleProductData = (productData) => {
        this.setState({product: productData});
        // console.log(this.state);
    }

    render() { 
        
        // console.log(this.props.match.params.productId);
        // console.log(this.state);

        return (
            <Router>
                <ScrollToTop /> 
                <Navbar totalCartItems={this.handleTotalCartItems}/>
                <Switch>
                    <Route exact path="/">
                        <Home
                            cart={this.state.cart} 
                            onIncrement={this.handleIncrement} 
                            onProductData={this.handleProductData}
                        />
                    </Route>
                    <Route exact path="/shop">
                        <div className="wrapper container mx-auto">
                            <Suspense fallback={<div>Loading ... </div>}>
                            <Shop
                                cart={this.state.cart} 
                                onIncrement={this.handleIncrement} 
                                onProductData={this.handleProductData}
                            />
                            </Suspense>
                        </div>
                    </Route>
                        <Route exact path="/shop/:productId/:encodedProductName">
                            <div className="wrapper container mx-auto">
                                <Product 
                                    cart={this.state.cart} 
                                    onIncrement={this.handleIncrement}
                                    product={this.state.product} 
                                />
                            </div>
                        </Route>
                    <Route exact path="/cart">
                        <div className="wrapper container mx-auto">
                            <Cart 
                                cart={this.state.cart}
                                onIncrement={this.handleIncrement}
                                onChange = {this.handleChange}
                                onDelete = {this.handleDelete}
                                onClearCart = {this.handleClearCart}
                            />
                        </div>
                    </Route>
                </Switch>
                <Footer/>
            </Router>
        );
    }
}

export default withRouter(App);
// solved by wrapping <App/> with <BrowserRouter> in index.js