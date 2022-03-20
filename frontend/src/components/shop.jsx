import React, { Component } from 'react';
import Products from './products';
import BreadCrumb from './breadcrumb';
import {productURL, getAllProducts} from '../callAPI/productAPI';

class Shop extends Component {
    // state = {
    //     products : [
    //         {productId: 2, productName: "Dog Tag", productPrice: 9.9, description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 10, imgSrc: './images/dog_tags2.jpg'},
    //         {productId: 3, productName: "Dog Tags", productPrice: 9.9, description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 5, imgSrc: './images/dog_tags3.jpg'},
    //         {productId: 4, productName: "Dog Tagss", productPrice: 9.9, description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 0, imgSrc: './images/dog_tags4.jpg'},
    //         {productId: 5, productName: "Food Bowl", productPrice: 9.9, description: 'This food bowl is made of brushed metal that is both durable and stylish.', stockCount: 3, imgSrc: './images/product5.jpg'},
    //         {productId: 6, productName: "Dog Elephant Toy", description: 'This toy is soft and durable, definitely a choice for all dogs', productPrice: 9.9, stockCount: 0, imgSrc: './images/product6.jpg'},
    //         {productId: 7, productName: "Braided Leash", description: 'The leash is braided using nylon, suitable for all dog sizes', productPrice: 9.9, stockCount: 9, imgSrc: './images/product7.jpg'},
    //     ]
    // }
    state = {}

    componentDidMount() {
        //1. API call to retrieve all product data
        //2. update the product in state with new data using setState
        // meaning call each API whenever use access each site
        //3. onRetrieveProductsData
        // this.props.onProductData(this.state.products);
        getAllProducts(productURL).then(result => {
            if (result.code == 200) {
                this.setState({"products": result.data});
            } else {
                console.log("code", result.code);
                console.log("error", result.data);
            }
        });
    }

    render() {
        const {products} = this.state;
        const {onIncrement, onProductData} = this.props;

        return (
            <React.Fragment>
                <div className="shop-banner mb-3 d-flex justify-content-center">
                    <h3 className="shop-banner-header">New Arrivals for the Season.</h3>
                </div>
                <BreadCrumb productName="" />
                <Products products={products} cart={this.props.cart} onIncrement={onIncrement} onProductData={onProductData}/>
            </React.Fragment>
        );
    }
}

export default Shop;