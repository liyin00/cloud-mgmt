import React, {Component} from 'react';
import Banner from './banner';
import Carousel from './carousel';
import {Link} from 'react-router-dom';
import {productURL, getAllProducts} from '../callAPI/productAPI';
import product from './product';


class Home extends Component {
    // state = {
    //     products: [
    //         {productId: 2, productName: "Food Bowl", description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 10, productPrice: 29.9, imgSrc: './images/dog_tags2.jpg'},
    //         {productId: 3, productName: "Braided Leash", description: 'The leash is braided using nylon, suitable for all dog sizes', stockCount: 5, productPrice: 19.9, imgSrc: './images/dog_tags3.jpg'},
    //         {productId: 4, productName: "Comfy Dog Bed", description: 'The bed is comfortable and soft ensuring a good nights rest', stockCount: 0, productPrice: 9.9, imgSrc: './images/dog_tags4.jpg'},
    //         {productId: 5, productName: "Food Bowls", description: 'This dog tag is made of brushed metal that is both durable and stylish.', stockCount: 3, productPrice: 9.9, imgSrc: './images/product5.jpg'},
    //         {productId: 6, productName: "Elephant Toy", description: 'This toy is soft and durable, definitely a choice for all dogs', stockCount: 0, productPrice: 19.9, imgSrc: './images/product6.jpg'},
    //         {productId: 7, productName: "Braided Leash", description: 'The leash is braided using nylon, suitable for all dog sizes', stockCount: 9, productPrice: 9.5, imgSrc: './images/product7.jpg'},
    //         {productId: 8, productName: "Comfy Dog Bed", description: 'The bed is comfortable and soft ensuring a good nights rest', stockCount: 2, productPrice: 8.5, imgSrc: './images/product8.jpg'},
    //         {productId: 9, productName: "Doggo Toy", description: 'This toy is soft and durable, definitely a choice for all dogs', stockCount: 8, productPrice: 7.5, imgSrc: './images/product9.jpg'},   
    //     ]
    // }

    state = {}

    componentDidMount() {
        // 1. API call for featured collection
        // 2. update state with new data invoked
        // let output = await getProductName(productURL, "p10");
        // console.log(output);
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
        const {cart, onIncrement, onProductData} = this.props;
        return (
            <React.Fragment>
                <Banner/>
                {/* <Featured products={this.state.products} cart={cart} onIncrement={onIncrement} /> */}
                <div className="container mt-5 mx-auto">
                    <Link to="/shop/dog-collection" className="collection">
                        <p>New Arrivals. </p>
                    </Link>
                    <Carousel products={this.state.products} cart={cart} onIncrement={onIncrement} onProductData={onProductData}/>
                </div>
            </React.Fragment>
        );
    }
}

export default Home;