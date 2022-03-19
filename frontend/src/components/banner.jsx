import React from 'react';

const Banner = () => {
    return (
        <React.Fragment>
            <div className="row banner m-0" id="banner-desk">
                <div className="col-lg-7 banner-img p-0">
                    {/* <img src="./images/dog_tags.jpg" alt=""/> */}
                    <img className="rounded banner-img-size" src="./images/banner_image_1.jpg" alt=""/>
                </div>
                <div className="col-lg-5 my-auto">
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
                </div>
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