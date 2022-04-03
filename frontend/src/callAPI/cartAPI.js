export const cartURL = "http://127.0.0.1:5006";

// ====== create ========
//Create payment
//sample
export async function createCartItem(URL, body) {
    try {
        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/create_cart_item`,data)
        if (response) {
            const result = await response.json()
            return result;
        }
    } catch(e) {
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}

export async function getCartByUserId(URL, userId) {
    try {
        const response = await fetch(`${URL}/get_cart_by_user_id/${userId}`);
        if (response) {
            const result = await response.json();
            return result;
        }
    } catch(e) {
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}


export async function modifyCart(URL, body) {
    try {
        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/modify_cart`,data)
        if (response) {
            const result = await response.json()
            return result;
        }
    } catch(e) {
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}