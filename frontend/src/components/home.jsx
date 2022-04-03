import React, {Component} from 'react';
import Banner from './banner';
import Carousel from './carousel';
import {Link} from 'react-router-dom';
import {productURL, getAllProducts} from '../callAPI/productAPI';

class Home extends Component {

    state = {
        products: []
    }

    componentDidMount() {
        const session = JSON.parse(sessionStorage.getItem("session"));
        if (session) {
            const user_id = session.user_id;
            if (user_id === "") {
                window.location.href = '/login.html';
            }
        } else {
            window.location.href = '/login.html';
        }
        // 1. API call for featured collection
        // 2. update state with new data invoked
        // let output = await getProductName(productURL, "p10");
        // console.log(output);
        getAllProducts(productURL).then(result => {
            if (result.code === 200) {
                this.setState({"products": result.data});
            } else {
                console.log("code", result.code);
                console.log("error", result.data);
            }
        });
        
    }

    render() {
        console.log(this.props.products)
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