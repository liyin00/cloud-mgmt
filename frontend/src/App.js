import React, { Component } from 'react';
import ScrollToTop from './components/scrollToTop'; //helps to reset scroll during page change
import Navbar from './components/navbar';
import Footer from './components/footer';
import Home from './components/home';
import Shop from './components/shop';
import Product from './components/product';
import Cart from './components/cart';
import './App.css';
import { BrowserRouter as Router, Route, Switch, withRouter  } from 'react-router-dom';
import {cartURL,createCartItem} from  './callAPI/cartAPI'

class App extends Component {
    state = {
        //retrieve cart items for sessionStorage
        //update state if cart item exists in sessionStorage

        cart: [],
        // {productId: 3, value: 1},
        // {productId: 4, value: 2}
        product: []
    };

    handleIncrement = (product, product_id) => {
        let product_data = {
            'user_id' : 'u6',
            'product_id' :  product_id,
            'product_name': product.product_name,
            'product_description': product.product_description,
            'product_img': product.product_img,
            'quantity':'1',
            'price' : product.price
        }
        createCartItem(cartURL, product_data).then(result => {
            console.log("result is ", result)
            if (result.code == 200) {
                this.setState({ alert: true });
                this.error = false;

                //copy cart items
                const cart = [...this.state.cart];
                const itemArray = this.state.cart.filter(item=>item.productId == product.productId);
                //create the value attribute in product
                if (itemArray.length === 0) {
                    product.value = 1;
                    cart.push(product);
                    this.setState({cart});
                }
                else {
                    const itemInCart = itemArray[0];
                    //ensure only max 5 products can be added to cart
                    if (itemInCart.value === 5 ) return;
                    const index = cart.indexOf(itemInCart);
                    cart[index] = {...itemInCart};
                    cart[index].value++;
                    this.setState({cart});
                }
                
            } else {
                console.log("test")
                this.error = true;
            }
            
        })

    }


    handleDelete = (product) => {
        const cart = [...this.state.cart];
        const index = cart.indexOf(product);
        cart[index] = {...product};
        cart.splice(index, 1);
        this.setState({cart});
        console.log(this.state.cart);
    }

    handleChange = (event, product) => {
        const cart = [...this.state.cart];
        const index = cart.indexOf(product);
        cart[index] = {...product};
        cart[index].value = Number(event.target.value);
        this.setState({cart});
    }

    handleTotalCartItems = () => {
        //calculate the sum of items
        return this.state.cart.map(item => item.value).reduce((a,b) => a + b, 0)
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
                        <div class="wrapper container mx-auto">
                            <Shop 
                                cart={this.state.cart} 
                                onIncrement={this.handleIncrement} 
                                onProductData={this.handleProductData}
                            />
                        </div>
                    </Route>
                        <Route exact path="/shop/:productId/:encodedProductName">
                            <div class="wrapper container mx-auto">
                                <Product 
                                    cart={this.state.cart} 
                                    onIncrement={this.handleIncrement}
                                    product={this.state.product} 
                                />
                            </div>
                        </Route>
                    <Route exact path="/cart">
                        <div class="wrapper container mx-auto">
                            <Cart 
                                cart={this.state.cart}
                                onIncrement={this.handleIncrement}
                                onChange = {this.handleChange}
                                onDelete = {this.handleDelete}
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