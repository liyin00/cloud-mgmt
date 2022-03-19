import React, { Component } from 'react';
import { URL, checkoutPayment } from '../callAPI/endpoint.js'
import { Link } from 'react-router-dom';

class Cart extends Component {
    state = {}

    renderTable() {
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
                    { this.props.cart.map(p => (
                        <tr key={ p.productId }>
                            <td className="px-0"><img className="cart-image" src={ p.imgSrc } alt="" /></td>
                            <td>{ p.productName }</td>
                            <td>S$ { p.productPrice.toFixed(2) }</td>
                            <td>
                                <select className="custom-select" value={ p.value } 
                                        onChange={ (event) => this.props.onChange(event, p) }>
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">3</option>
                                    <option value="4">4</option>
                                    <option value="5">5</option>
                                </select>
                            </td>
                            <td>
                                S$ { (p.value * p.productPrice).toFixed(2) }
                                <br /><br /><br /><br /><br />
                                <Link onClick={this.props.onDelete}>
                                    <u className="text-danger">Remove Item</u>
                                </Link>
                                
                            </td>
                        </tr>
                    )) }
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td><b>Total</b>: S$ {(this.props.cart.map(p => Number((p.value * p.productPrice).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td>
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
                                    <select className="custom-select ml-2" value={ p.value } 
                                            onChange={ (event) => this.props.onChange(event, p) }>
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
                        <td><b>Total</b>: S$ {(this.props.cart.map(p => Number((p.value * p.productPrice).toFixed(2)))).reduce((a,b) => a+b).toFixed(2)}</td>
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
        this.renderTableMobile();
    }

    render() {
        
        return (
            <div className='cart-page-margin'>
                <h3>My Shopping Cart</h3>
                { this.props.cart.length > 0 ? this.renderTable()
                : <div className="cart-page tertiary-bg">
                    <p>Your shopping cart is currently empty.</p>
                    <Link to="/shop" className="btn primary-bg ml-3">Continue Shopping</Link>
                </div>
                    }
                
                { this.props.cart.length > 0 && this.renderTableMobile() }
            </div>
            
        );
    }
}

export default Cart;