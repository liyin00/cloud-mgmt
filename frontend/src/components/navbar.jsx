import React from 'react';
import {Link} from 'react-router-dom';

const Navbar = ({totalCartItems}) => {
    return (
        <nav className="navbar sticky-top navbar-expand-lg navbar-light">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <Link className="navbar-brand navbar-name pt-0" to="/">clåe.sg</Link>

            {/* Different Cart sequence orientation for different viewpoints */}
            <Link id="cart1" to="/cart">
                <span className="iconify cart" data-icon="mdi:cart" data-inline="false"></span>
                <span className="badge badge-pill badge-primary cart-count" >{totalCartItems()}</span>
            </Link> 

            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav mx-auto">
                    <li className="nav-item active">
                        <Link className="nav-link" to="/">Home<span className="sr-only">(current)</span></Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" to="/shop/new-arrivals">New Arrivals</Link>
                    </li>
                    <li className="nav-item dropdown">
                        <Link className="nav-link dropdown-toggle" to="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Shop
                        </Link>
                        <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <Link className="dropdown-item" to="/shop/dog-collection">Dog Collection</Link>
                            <Link className="dropdown-item" to="/shop/cat-collection">Cat Collection</Link>
                            <Link className="dropdown-item" to="/shop">All</Link>
                        </div>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" href="/pricing">Pricing</Link>
                    </li>
                    <li className="nav-item">
                        <Link className="nav-link" href="/faq">FAQ</Link>
                    </li>
                </ul>
            </div>

            <Link id="cart2" to="/cart">
                <span className="iconify cart" data-icon="mdi:cart" data-inline="false"></span>
                <span className="badge badge-pill badge-primary cart-count" >
                    {totalCartItems()}
                </span>
            </Link> 
            
        </nav>
        
    );
}

export default Navbar;

