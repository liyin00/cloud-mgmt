export const cartURL = "http://127.0.0.1:5006";

// ====== create ========
//Create payment
//sample
export async function createCartItem(URL, body) {
    try {
        console.log("inside cart api")
        console.log(body)
        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/create_cart_item`,data)
        if (response) {
            console.log("SUCCESS")
            const result = await response.json()
            return result;
        }
    } catch(e) {
        console.log("ERROR")
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}

export async function getCartByUserId(URL, userId) {
    try {
        console.log("asdass")
        const response = await fetch(`${URL}/get_cart_by_user_id/${userId}`);
        console.log("response is " )
        console.log(response)
        if (response) {
            console.log("enter if ")
            const result = await response.json();
            return result;
        }
    } catch(e) {
        console.log("catch error ")
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}


export async function modifyCart(URL, body) {
    try {
        console.log("inside cart api")
        console.log(body)
        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/modify_cart`,data)
        if (response) {
            console.log("SUCCESS")
            const result = await response.json()
            return result;
        }
    } catch(e) {
        console.log("ERROR")
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}