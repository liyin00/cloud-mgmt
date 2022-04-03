import React, { Component } from 'react';
import { paymentURL, checkoutPayment } from '../callAPI/paymentAPI.js'
import { Link, NavLink } from 'react-router-dom';
import {cartURL, getCartByUserId, modifyCart} from  '../callAPI/cartAPI'

class Cart extends Component {
    state = {
        cart: [],
        user_id: "",
        successAlert: false,
        errorAlert: false,
        alertMsg: ""
    }

    componentDidMount() {
        const session = JSON.parse(sessionStorage.getItem("session"));
        if (session) {
            this.setState({user_id: session.user_id});
        } else {
            window.location.href = "/login.html";
        }

        if (this.state.cart.length === 0) {
            getCartByUserId(cartURL,this.state.user_id).then(result => {
                if (result.code == 200) {
                    this.error = false;
                    const response = result.data;
                    if (response){
                        this.setState({
                            "cart": response.product_list,
                            "user_id": response.user_id
                        })       
                    }
                } else {
                    console.log("Error getting cart data", result);
                }
            });
        }
        //check the url for success and cancelled
        const query = new URLSearchParams(window.location.search);
        if (query.get("success")) {
            const body = {
                result: {
                    "product_list": [],
                    "user_id": this.state.user_id
                }
            }
            // this.props.onClearCart();
            // modifyCart(cartURL, body).then(result => {
            //     console.log(result)
            //     if (result.code === 200){
            //         console.log("heloOOOoOOO PLSSS")
            //         this.state.cart = []
            //         this.setState(this.state);
            //         console.log("Modified state:", this.state)
            //     } else {
            //         console.log("Error in deleting product from cart", result.data);
            //         this.error = true;
            //     }
            // });

            const msg = "Order placed. You will receive an email."
            this.state.successAlert = true;
            this.state.alertMsg = msg;
            this.setState(this.state);

        } if(query.get("cancelled")) {
            const msg = "Order cancelled. Continue to shop around!"
            this.state.errorAlert = true;
            this.state.alertMsg = msg
            this.setState(this.state)

        }

        console.log("before get Cart:", this.state)

        // if (this.state.cart.length === 0) {
        //     getCartByUserId(cartURL,"u6").then(result => {
        //         if (result.code == 200) {
        //             this.error = false;
        //             const response = result.data;
        //             if (response){
        //                 this.setState({
        //                     "cart": response.product_list,
        //                     "user_id": response.user_id
        //                 })       
        //             }
        //         } else {
        //             console.log("Error getting cart data", result);
        //         }
        //     });
        //     console.log("after get Cart:", this.state)
    
        // }

        
        


        // if (query.get("success")) {
        //     const msg = "Order placed. You will receive an email."
        //     this.state.successAlert = true;
        //     this.state.alertMsg = msg;
        //     this.setState(this.state);
        // }
        // if (query.get("cancelled")) {
        //     const msg = "Order cancelled. Continue to shop around!"
        //     this.state.errorAlert = true;
        //     this.state.alertMsg = msg
        //     this.setState(this.state)
        // }

    }

    componentDidUpdate(){
        if (this.state.cart !== this.props.cart){
            this.setState({"cart": this.props.cart});
        }
    }

    renderSuccessAlert(){
        if (this.state.successAlert){
            //clear cart of successful
            return <div class="alert alert-success alert-dismissible fade show py-3 w-100" role="alert">
            <strong>{ this.state.alertMsg }</strong>
            <button type="button" className="close" data-dismiss="alert" >
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        }
    }

    renderErrorAlert(){
        if (this.state.errorAlert){
            return <div class="alert alert-danger alert-dismissible fade show py-3 w-100" role="alert">
            <strong>{ this.state.alertMsg }</strong>
            <button type="button" className="close" data-dismiss="alert" >
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        }
    }

    createReqBody(){
        return {
            "cart": this.state.cart,
            "user_id":this.state.user_id
        }
    }

    modifyCartByUserId(){
        modifyCart(cartURL, this.state).then(result => {
            if (result.code == 200) {

                this.error = false;
                //const courses = result.data;
                
                //sort courses according to course id in ascending order
                
            } else {
                this.error = true;
            }
        });
    }


    changeCartQuantity(array_obj, quantity){
        var position = this.state.result.product_list.indexOf(array_obj);
        this.state.result.product_list[position].quantity = quantity
        this.setState(this.state);
        this.modifyCartByUserId();

    }

    deleteItem(product_obj){
        var position = this.state.result.product_list.indexOf(product_obj);
        this.state.result.product_list.splice(position,1)
        this.setState(this.state);
        this.modifyCartByUserId();
    }


    renderTable() {
        var counter = 0 
        return (
            <div className="cart-page-desk">
                <table className='table mt-3'>
                <tfoot>
                    <tr className="tertiary-bg">
                        <td>Product</td>
                        <td>Details</td>
                        <td>Unit Price</td>
                        <td>Quantity</td>
                        <td>Subtotal</td>
                    </tr>
                    { this.state.cart.map(p => (
                        
                        <tr key={ p.product_id }>
                            <td className="px-0"><img className="cart-image" src={ p.product_img } alt="" /></td>
                            <td>{ p.product_name }</td>
                            <td>S$ { Number(p.price).toFixed(2) }</td>
                            <td>
                                {/* <select className="custom-select" onChange={(event) => this.changeCartQuantity(p, event.target.value)} value={p.quantity}  > */}
                                <select className="custom-select" onChange={(event) => this.props.onChange(p, event.target.value)} value={p.quantity}  >
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            <td>
                                S$ { (p.quantity * p.price).toFixed(2) }
                                <br /><br /><br /><br /><br />
                                {/* <Link onClick={(event) => this.deleteItem(p)}> */}
                                <Link onClick={() => this.props.onDelete(p) }>
                                    <u className="text-danger">Remove Item</u>
                                </Link>
                                
                            </td>
                        </tr>
                        
                    )

                    ) 
                    
                    }
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {/* <td><b>Total</b>: S$ {(this.state.result.product_list.map(p => Number((p.quantity * p.price).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td> */}
                        <td><b>Total</b>: S$ {(this.state.cart.map(p => Number((p.quantity * p.price).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td>
                    </tr>
                </tfoot>
                </table>
                {/* <form action={`${paymentURL}/create-checkout-session`} method="POST">
                    <button className="btn primary-bg d-flex justify-content-center" type="submit">
                        Checkout
                    </button>
                </form> */}
                {/* checkoutPayment */}
                <button className="btn primary-bg d-flex justify-content-center" onClick={() => checkoutPayment(paymentURL, this.createReqBody())} disabled={this.state.cart.length===0 ? true: false} type="submit">
                    Checkout
                </button>
            </div>
        );
    }

    renderTableMobile() {
        return (
            <div className="cart-page-mobile">
                <table className='table mt-3'>
                <tfoot>
                    <tr className="tertiary-bg">
                        <td>Product</td>
                        <td>Details</td>
                    </tr>
                    { this.props.cart.map(p => (
                        <tr key={ p.productId }>
                            <td className="px-0"><img className="cart-image" src={ p.imgSrc } alt="" /></td>
                            <td>
                                <p><b>{ p.productName }</b></p>
                                <p>Unit Price: S$ { p.productPrice.toFixed(2) }</p>
                                <div className="mb-3">
                                    Qty:
                                    <select className="custom-select ml-2"  value={ p.quantity } 
                                            onChange={ (event) => this.change_cart_quantity(p,p.quantity, event.target.value)}>
                                        <option value="1">1</option>
                                        <option value="2">2</option>
                                        <option value="3">3</option>
                                        <option value="4">4</option>
                                        <option value="5">5</option>
                                    </select> 
                                </div>
                                <p>Subtotal: S$ { (p.value * p.productPrice).toFixed(2) }</p>
                                <Link onClick={this.props.onDelete(p)}>
                                    <u className="text-danger">Remove Item</u>
                                </Link>
                            </td>
                        </tr>
                    )) }
                    <tr>
                        <td></td>
                        {/* <td><b>Total</b>: S$ {(this.props.cart.map(p => Number((p.value * p.productPrice).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td> */}
                    </tr>
                </tfoot>
                </table>
                <div className="">
                    <a className="btn font-weight-light text-white primary-bg d-flex justify-content-center">Check out</a>
                </div>
            </div>
        );
    }

    renderAllTables() {
        this.renderTable();
        // this.renderTableMobile();
    }

    render() {
        if(Object.keys(this.state).length === 0 ){
            return null
        } else{
            return (
                <div>
                    <div className='cart-page-margin'>
                        <h3>My Shopping Cart</h3>
                        {this.renderSuccessAlert()}
                        {this.renderErrorAlert()}
                        {this.state.cart.length > 0 ? this.renderTable()
                        : <div className="cart-page tertiary-bg">
                            <p>Your shopping cart is currently empty.</p>
                            <Link to="/shop" className="btn primary-bg ml-3">Continue Shopping</Link>
                        </div>
                            }
                        {/* { this.state.result.product_list.length > 0 && this.renderTableMobile() } */}
                    </div>
                </div>
                
            );
        }
        

    }
}

export default Cart;