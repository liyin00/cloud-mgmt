import React from 'react';

const Footer = () => {
    return (
        <footer>
            <div className="container">
                <div className="row mx-auto">
                    <div className="col-lg-4 col-6">
                        <h5>Quick Links</h5>
                        <ul className="footer-list">
                            <li><a href="#">Shipping Fee</a></li>
                            <li><a href="#">Shop</a></li>
                            <li><a href="#">FAQ</a></li>
                            <li><a href="#">About Us</a></li>
                        </ul>
                    </div>
                    <div className="col-lg-4 col-6">
                        <h5>Contact Us</h5>
                        <ul className="footer-list">
                            <li className="mb-1"><a href="#">
                                <span className="iconify icon" data-icon="akar-icons:instagram-fill"></span>clae.sg
                            </a></li>
                            <li><a href="#">
                                <span className="iconify icon" data-icon="logos:tiktok-icon"></span>clae.sg
                            </a></li>
                        </ul>
                    </div>
                    <div className="col-lg-4 col-12">
                        <div className="newsletter-input">
                            <h5>Subscribe to our newsletter.</h5>
                            <div className="input-group my-3">
                                <input type="text" className="form-control" placeholder="Your Email"/>
                                <div className="input-group-append">
                                    <button className="btn" type="button" id="newsletter-button">Submit</button>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
    </footer>
    );
}

export default Footer;