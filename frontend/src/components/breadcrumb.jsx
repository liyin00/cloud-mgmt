import React from 'react';
import {Link} from 'react-router-dom';

const BreadCrumb = ({productName}) => {
    return (
        <div>
            <ol className="breadcrumb">
                <li className="breadcrumb-item"><Link to="/shop">Shop</Link></li>
                <li className="breadcrumb-item active">{ productName }</li>
            </ol>
        </div>
    );
}

export default BreadCrumb;