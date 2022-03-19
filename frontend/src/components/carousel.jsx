import React, { Component } from 'react';
import Card from './card';

class Carousel extends Component {
    state = {};

    numCarouselSlides = () => {
        const numSlides = Math.ceil(this.props.products.length / 3);
        return [...Array(numSlides).keys()];
    }

    numProductsArray = () => {
        const numProducts = [...Array(this.props.products.length).keys()];
        return this.numCarouselSlides().map(num => (
                num !== this.numCarouselSlides() - 1 ? numProducts.splice(0, 3) : numProducts
            ));   
    }

    formatIndicatorsClass = (index) => {
        let className = '';
        if (index === 0) {className = 'active'};
        return className;
    }

    formatCarouselItemClass = (index) => {
        let className = 'carousel-item';
        if (index === 0) className += ' active';
        return className;
    }

    render() {
        const {cart, onIncrement, products, onProductData} = this.props;
        const {productId} = products;

        return ( 
            <div>
                <div id="carouselExampleIndicators" className="carousel slide" data-ride="carousel" data-interval="false">
                    <ol className="carousel-indicators">
                        {this.numCarouselSlides().map(num => (
                            <li key={num} data-target="#carouselExampleIndicators" data-slide-to={num} className={this.formatIndicatorsClass(num)} ></li>
                        ))}
                    </ol>
                    <div className="carousel-inner">
                        {this.numProductsArray().map((group, index) => (
                            <div className={this.formatCarouselItemClass(index)}>
                                <div className="row mb-4">
                                    {group.map(i => (
                                        <div className="col-4 carousel-card" key={productId} >
                                            <Card product={products[i]} cart={cart} onIncrement={onIncrement} onProductData={onProductData} />
                                        </div>
                                    ))}
                                </div>
                            </div>
                        ))}                        
                    </div>

                    <a className="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span className="sr-only">Previous</span>
                    </a>
                    <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span className="carousel-control-next-icon" aria-hidden="true"></span>
                        <span className="sr-only">Next</span>
                    </a>
                </div>
        </div>
        );
    }
}

export default Carousel;