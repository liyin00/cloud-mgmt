import React from 'react';
import {Link} from 'react-router-dom';

const Banner = () => {
    return (
        <React.Fragment>
            <div className="row m-0" id="banner-desk">
                <div className="col-lg-12 banner-img p-0">
                    {/* <img src="./images/dog_tags.jpg" alt=""/> */}
                    <img className="rounded img-fluid w-100" src="./images/banner.png" alt=""/>
                    <div className="banner-text">
                        <h1 className="display-4">Seasonal Style for every occasion.</h1>
                        <Link to="/shop">
                            <button className="btn primary-bg font-weight-bold py-2 px-4 mt-2">Shop Now</button>
                        </Link>
                    </div>
                </div>
                {/* <div className="col-lg-5 my-auto">
                    <div className="banner-header">
                        <p>About Us</p>
                        <h1>Clåe.sg pet tags.</h1>
                        <p>
                            A one-of-a-kind realistic & customizable pet portrait.<br/>
                            One-stop-shop for pet products.
                        </p>
                        <a className="btn btn-outline-secondary mt-2">
                            <div className="d-flex">
                                <span className="iconify icon" data-icon="akar-icons:instagram-fill"></span>DM us @clae.sg
                            </div>
                        </a>
                    </div>
                </div> */}
            </div>

            <div id="banner-mobile">
                <div className="banner" >
                    <div className="banner-image">
                        <img src="./images/dog_tags.jpg" height="100%" width="auto" alt=""/>
                    </div>
                </div>
                <div className="banner-header">
                    <p>About Us</p>
                    <h1>Clåe.sg pet tags.</h1>
                    <p>
                        A one-of-a-kind realistic & customizable pet portrait. <br/>
                        One-stop-shop for pet products.
                    </p>
                    {/* <a className="btn btn-outline-secondary mt-2">
                        <div className="d-flex">
                            <span className="iconify icon" data-icon="akar-icons:instagram-fill"></span>DM us @clae.sg
                        </div>
                    </a> */}
                </div>
            </div>
        </React.Fragment>
        

    );
}

export default Banner;