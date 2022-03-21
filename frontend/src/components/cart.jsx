import React, { Component } from 'react';
import { URL, checkoutPayment } from '../callAPI/paymentAPI.js'
import { Link, NavLink } from 'react-router-dom';
import {cartURL,getCartByUserId,modifyCart} from  '../callAPI/cartAPI'

class Cart extends Component {
    state = {}

    componentDidMount() {
        console.log("run first")
        // 1. API call for featured collection
        // 2. update state with new data invoked
        // fetch(cartURL,"p2")
        //     .then(response => response.json())
        //     .then(data => this.setState({ totalReactPackages: data.total }));
        // console.log(test)
        //HARDCODE
        getCartByUserId(cartURL,"u6").then(result => {
            if (result.code == 200) {

                console.log('result is')
                console.log(result.data)
                this.error = false;
                const courses = result.data;

                this.setState(
                    {result:result.data}
                )
                
                //sort courses according to course id in ascending order
                
            } else {
                console.log("test")
                this.error = true;
            }
        });


    }

    modifyCartByUserId(){
        modifyCart(cartURL, this.state).then(result => {
            console.log("result is ", result)
            if (result.code == 200) {

                console.log('result is')
                console.log(result.data)
                this.error = false;
                //const courses = result.data;
                
                //sort courses according to course id in ascending order
                
            } else {
                console.log("test")
                this.error = true;
            }
        });
    }


    changeCartQuantity(array_obj, quantity){
        console.log(array_obj)
        var position = this.state.result.product_list.indexOf(array_obj);
        console.log("in change cart quantity, position is " , position)
        console.log("previous quantity" , this.state.result.product_list[position].quantity)
        this.state.result.product_list[position].quantity = quantity
        console.log("after quantity" , this.state.result.product_list[position].quantity)
        this.setState(this.state);
        this.modifyCartByUserId();

        // this.renderTableMobile();

    }

    deleteItem(product_obj){
        console.log('delete item');
        var position = this.state.result.product_list.indexOf(product_obj);
        this.state.result.product_list.splice(position,1)
        this.setState(this.state);
        this.modifyCartByUserId();
        console.log(this.state);
        



    }

    renderTable() {
        console.log(this.state)
        console.log("run second")
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
                    { this.state.result.product_list.map(p => (
                        
                        <tr key={ p.product_id }>
                            <td className="px-0"><img className="cart-image" src={ p.product_img } alt="" /></td>
                            <td>{ p.product_name }</td>
                            <td>S$ { Number(p.price).toFixed(2) }</td>
                            <td>
                                <select className="custom-select" onChange={(event) => this.changeCartQuantity(p, event.target.value)} value={p.quantity}  >
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
                                <Link onClick={(event) => this.deleteItem(p)}>
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
                        <td><b>Total</b>: S$ {(this.state.result.product_list.map(p => Number((p.quantity * p.price).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td>
                    </tr>
                </tfoot>
                </table>
                {/* <form action={`${URL}/create-checkout-session`} method="POST">
                    <button className="btn primary-bg d-flex justify-content-center" type="submit">
                        Checkout
                    </button>
                </form> */}
                {/* checkoutPayment */}
                <button className="btn primary-bg d-flex justify-content-center" onClick={() => checkoutPayment(URL, this.props.cart)} type="submit">
                    Checkout
                </button>
            </div>
        );
    }

    renderTableMobile() {
        console.log('MObile view');
        console.log(this.state);
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
                                <Link onClick={this.props.onDelete}>
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
        console.log("come here render")
        if(Object.keys(this.state).length === 0 ){
            console.log("herehehrehrhehreh nothing")
            return null
        }else{
            console.log("value below")
            console.log(this.state)
            console.log(this.state.result.product_list.length)
            return (
                <div className='cart-page-margin'>
                    <h3>My Shopping Cart</h3>
                    {this.state.result.product_list.length > 0 ? this.renderTable()
                    : <div className="cart-page tertiary-bg">
                        <p>Your shopping cart is currently empty.</p>
                        <Link to="/shop" className="btn primary-bg ml-3">Continue Shopping</Link>
                    </div>
                        }
                    
                    {/* { this.state.result.product_list.length > 0 && this.renderTableMobile() } */}
                </div>
                
            );
        }
        

     

    }
}

export default Cart;